import json
import datetime
from web3 import Web3
from web3.exceptions import BlockNotFound
from project.nft.models import NFT
from project.settings import (
  RPC_URL,
  IS_TESTNET,
  CONTRACT_ADDRESS,
  BASE_DIR,
  INITIAL_ETHEREUM_BLOCK_NUMBER
)
from project.contract_history.models import TransferHistory, ScannerState


TESTNET_ABI_PATH = str(BASE_DIR) + "/project/utils/TESTNET_ABI.json"
MAINNET_ABI_PATH = str(BASE_DIR) + "/project/utils/MAINNET_ABI.json"

NULL_ADDRESS = "0x0000000000000000000000000000000000000000"



class Scanner:
  def __init__(self):
    self.default_max_chunk_for_iteration = 10
    self.contract_addr = CONTRACT_ADDRESS
    self.rpc_url = RPC_URL
    abi_file = open(TESTNET_ABI_PATH) if IS_TESTNET else open(MAINNET_ABI_PATH)
    self.abi = json.load(abi_file)
    self.web3 = Web3(Web3.HTTPProvider(self.rpc_url))
    self.contract_address = Web3.toChecksumAddress(CONTRACT_ADDRESS)
    self.contract = self.web3.eth.contract(self.contract_address, abi=self.abi)


  def fetch_data(self, start_block, end_block):
    transfer_events = self.contract.events.Transfer()
    filter_builder = transfer_events.build_filter()
    filter_builder.fromBlock = start_block
    filter_builder.toBlock = end_block
    filter_instance = filter_builder.deploy(self.web3)
    transfer_data = filter_instance.get_all_entries()
    transfer_data = Web3.toJSON(transfer_data)
    transfer_data = json.loads(transfer_data)

    for data in transfer_data:
        print("###", data["args"])
        print("$$$", data["event"])
        print("IIII", data["transactionHash"])
        print("OOOO", data["blockNumber"])
    print(BASE_DIR)
    return "success", transfer_data

  def get_initial_block(self):
    # get from database
    try:
      record = ScannerState.objects.latest("created_at")
      print(f"Restored the state, previously {record.last_scanned_block} blocks have been scanned")
      return record.last_scanned_block
    except ScannerState.DoesNotExist:
      print("State starting from scratch")
      if IS_TESTNET:
        return 0
      else:
        return INITIAL_ETHEREUM_BLOCK_NUMBER

  def get_block_timestamp(self, block_num):
    try:
      block_info = self.web3.eth.getBlock(block_num)
    except BlockNotFound:
      return None
    last_time = block_info["timestamp"]
    return datetime.datetime.utcfromtimestamp(last_time)

  def store_data(self, data):
    print(data)
    for d in data:
      # TODO: aggregate OpenSee Transfers
      timestamp = self.get_block_timestamp(d["blockNumber"])
      TransferHistory.objects.update_or_create(
        block_number=d["blockNumber"],
        from_address=d["args"].get("from"),
        to_address=d["args"].get("to"),
        from_ens=None,
        to_ens=None,
        tx_hash=d["transactionHash"],
        token_id=d["args"].get("tokenId"),
        timestamp=timestamp,
        defaults={},
      )
      ScannerState.objects.update_or_create(defaults={"last_scanned_block": d["blockNumber"]})
      # mint from zero
      if d["args"].get("from") == NULL_ADDRESS:
        NFT.objects.update_or_create(
          defaults={"token_id": d["args"].get("tokenId")}
        )
      # burn
      if d["args"].get("to") == NULL_ADDRESS:
        NFT.objects.filter(token_id=d["args"].get("tokenId")).update(deleted_at=timestamp)

  def run(self):

    init_block = self.get_initial_block()
    end_block = self.web3.eth.blockNumber
    if not IS_TESTNET:
      end_block = end_block - 10

    if not init_block < end_block and not init_block + \
           self.default_max_chunk_for_iteration < end_block:
      return
    # TODO: need 3 or 5 retry to break down chunk
    status, data = self.fetch_data(init_block, init_block + self.default_max_chunk_for_iteration)
    if status == "success":
      self.store_data(data)

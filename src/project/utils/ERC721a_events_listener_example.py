from web3 import Web3
from web3._utils.events import get_event_data

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/9317e901ece9489c8fa9b44078283316"))

az_token_addr = "0xED5AF388653567Af2F388E6224dC7C4b3241C544"
az_abi = [
    {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
        {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "Transfer",
                                                              "type": "event"}]

ck_contract = w3.eth.contract(address=w3.toChecksumAddress(az_token_addr), abi=az_abi)
# name = ck_contract.functions.name().call()
# symbol = ck_contract.functions.symbol().call()

# print(f"{name} {symbol}")


transfer_az_abi = {
    "anonymous": False,
    'inputs': [
        {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
        {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}
    ],
    "name": "Transfer",
    "type": "event"
}

ownership_transfer_az_abi = {
    "anonymous": False,
    "inputs": [
        {"indexed": True, "internalType": "address", "name": "previousOwner", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "newOwner", "type": "address"}
    ],
    "name": "OwnershipTransferred",
    "type": "event"
}



# We need the event's signature to filter the logs
event_signature = w3.sha3(text="Transfer(address,address,uint256)").hex()
# 9820
# 6510
# 4032
# 9561
# 2608
# 2468
# 1449
# 1959
print(w3.eth.blockNumber - 696225)
logs1 = w3.eth.get_logs({
    "fromBlock": w3.eth.blockNumber - 800000,
    "toBlock":w3.eth.blockNumber - 696000,
    "address": w3.toChecksumAddress(az_token_addr),
    "topics": [event_signature]
})

recent_tx = [get_event_data(w3.codec, transfer_az_abi, log)["args"] for log in logs1]

print(len(recent_tx))

# for tx in recent_tx:
#     print(tx["from"], tx["to"], tx['tokenId'])

#
# event_signature2 = w3.sha3(text="transferOwnership(address,address)").hex()
#
# logs2 = w3.eth.get_logs({
#     "fromBlock": w3.eth.blockNumber - 500,
#     "address": w3.toChecksumAddress(az_token_addr),
#     "topics": [event_signature2]
# })
#
#
# ownership_transfer_tx = [get_event_data(w3.codec, ownership_transfer_az_abi, log)["args"] for log in logs2]
# print("Ownership transfer")
# for tx in ownership_transfer_tx:
#     print(tx["previousOwner"], tx["newOwner"])
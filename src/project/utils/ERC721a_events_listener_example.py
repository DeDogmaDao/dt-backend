from web3 import Web3
from web3._utils.events import get_event_data

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/9317e901ece9489c8fa9b44078283316"))

az_token_addr = "0xED5AF388653567Af2F388E6224dC7C4b3241C544"
az_abi = [
    {"inputs": [{"internalType": "uint256", "name": "maxBatchSize_", "type": "uint256"},
                      {"internalType": "uint256", "name": "collectionSize_", "type": "uint256"},
                      {"internalType": "uint256", "name": "amountForAuctionAndDev_", "type": "uint256"},
                      {"internalType": "uint256", "name": "amountForDevs_", "type": "uint256"}],
    "stateMutability": "nonpayable","type": "constructor"},
    {"anonymous": False, "inputs": [
                        {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
                        {"indexed": True, "internalType": "address", "name": "approved", "type": "address"},
                        {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}],
     "name": "Approval", "type": "event"}, {"anonymous": False, "inputs": [
    {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
    {"indexed": True, "internalType": "address", "name": "operator", "type": "address"},
    {"indexed": False, "internalType": "bool", "name": "approved", "type": "bool"}], "name": "ApprovalForAll",
                                                                                        "type": "event"},
          {"anonymous": False,
           "inputs": [{"indexed": True, "internalType": "address", "name": "previousOwner", "type": "address"},
                      {"indexed": True, "internalType": "address", "name": "newOwner", "type": "address"}],
           "name": "OwnershipTransferred", "type": "event"}, {"anonymous": False, "inputs": [
        {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
        {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
        {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "Transfer",
                                                              "type": "event"},
          {"inputs": [], "name": "AUCTION_DROP_INTERVAL",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"}, {"inputs": [], "name": "AUCTION_DROP_PER_STEP",
                                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                 "stateMutability": "view", "type": "function"},
          {"inputs": [], "name": "AUCTION_END_PRICE",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"}, {"inputs": [], "name": "AUCTION_PRICE_CURVE_LENGTH",
                                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                 "stateMutability": "view", "type": "function"},
          {"inputs": [], "name": "AUCTION_START_PRICE",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"},
          {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "allowlist",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"},
          {"inputs": [], "name": "allowlistMint", "outputs": [], "stateMutability": "payable", "type": "function"},
          {"inputs": [], "name": "amountForAuctionAndDev",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"}, {"inputs": [], "name": "amountForDevs",
                                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                 "stateMutability": "view", "type": "function"}, {
              "inputs": [{"internalType": "address", "name": "to", "type": "address"},
                         {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "approve",
              "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "quantity", "type": "uint256"}], "name": "auctionMint",
           "outputs": [], "stateMutability": "payable", "type": "function"},
          {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "balanceOf",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "quantity", "type": "uint256"}], "name": "devMint",
           "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
              "inputs": [{"internalType": "uint64", "name": "mintlistPriceWei", "type": "uint64"},
                         {"internalType": "uint64", "name": "publicPriceWei", "type": "uint64"},
                         {"internalType": "uint32", "name": "publicSaleStartTime", "type": "uint32"}],
              "name": "endAuctionAndSetupNonAuctionSaleInfo", "outputs": [], "stateMutability": "nonpayable",
              "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "getApproved",
           "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view",
           "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_saleStartTime", "type": "uint256"}],
                                 "name": "getAuctionPrice",
                                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                 "stateMutability": "view", "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "getOwnershipData",
           "outputs": [{"components": [{"internalType": "address", "name": "addr", "type": "address"},
                                       {"internalType": "uint64", "name": "startTimestamp", "type": "uint64"}],
                        "internalType": "struct ERC721A.TokenOwnership", "name": "", "type": "tuple"}],
           "stateMutability": "view", "type": "function"}, {
              "inputs": [{"internalType": "address", "name": "owner", "type": "address"},
                         {"internalType": "address", "name": "operator", "type": "address"}],
              "name": "isApprovedForAll", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
              "stateMutability": "view", "type": "function"}, {
              "inputs": [{"internalType": "uint256", "name": "publicPriceWei", "type": "uint256"},
                         {"internalType": "uint256", "name": "publicSaleKey", "type": "uint256"},
                         {"internalType": "uint256", "name": "publicSaleStartTime", "type": "uint256"}],
              "name": "isPublicSaleOn", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
              "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "maxPerAddressDuringMint",
                                                               "outputs": [{"internalType": "uint256", "name": "",
                                                                            "type": "uint256"}],
                                                               "stateMutability": "view", "type": "function"},
          {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
           "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "nextOwnerToExplicitlySet",
                                                            "outputs": [{"internalType": "uint256", "name": "",
                                                                         "type": "uint256"}], "stateMutability": "view",
                                                            "type": "function"},
          {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "numberMinted",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"},
          {"inputs": [], "name": "owner", "outputs": [{"internalType": "address", "name": "", "type": "address"}],
           "stateMutability": "view", "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "ownerOf",
           "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view",
           "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "quantity", "type": "uint256"},
                                            {"internalType": "uint256", "name": "callerPublicSaleKey",
                                             "type": "uint256"}], "name": "publicSaleMint", "outputs": [],
                                 "stateMutability": "payable", "type": "function"},
          {"inputs": [], "name": "renounceOwnership", "outputs": [], "stateMutability": "nonpayable",
           "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"},
                                            {"internalType": "address", "name": "to", "type": "address"},
                                            {"internalType": "uint256", "name": "tokenId", "type": "uint256"}],
                                 "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable",
                                 "type": "function"}, {
              "inputs": [{"internalType": "address", "name": "from", "type": "address"},
                         {"internalType": "address", "name": "to", "type": "address"},
                         {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
                         {"internalType": "bytes", "name": "_data", "type": "bytes"}], "name": "safeTransferFrom",
              "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "saleConfig",
                                                                                    "outputs": [
                                                                                        {"internalType": "uint32",
                                                                                         "name": "auctionSaleStartTime",
                                                                                         "type": "uint32"},
                                                                                        {"internalType": "uint32",
                                                                                         "name": "publicSaleStartTime",
                                                                                         "type": "uint32"},
                                                                                        {"internalType": "uint64",
                                                                                         "name": "mintlistPrice",
                                                                                         "type": "uint64"},
                                                                                        {"internalType": "uint64",
                                                                                         "name": "publicPrice",
                                                                                         "type": "uint64"},
                                                                                        {"internalType": "uint32",
                                                                                         "name": "publicSaleKey",
                                                                                         "type": "uint32"}],
                                                                                    "stateMutability": "view",
                                                                                    "type": "function"}, {
              "inputs": [{"internalType": "address[]", "name": "addresses", "type": "address[]"},
                         {"internalType": "uint256[]", "name": "numSlots", "type": "uint256[]"}],
              "name": "seedAllowlist", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {
              "inputs": [{"internalType": "address", "name": "operator", "type": "address"},
                         {"internalType": "bool", "name": "approved", "type": "bool"}], "name": "setApprovalForAll",
              "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [{"internalType": "uint32", "name": "timestamp", "type": "uint32"}],
           "name": "setAuctionSaleStartTime", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [{"internalType": "string", "name": "baseURI", "type": "string"}], "name": "setBaseURI",
           "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "quantity", "type": "uint256"}], "name": "setOwnersExplicit",
           "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [{"internalType": "uint32", "name": "key", "type": "uint32"}], "name": "setPublicSaleKey",
           "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [{"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}], "name": "supportsInterface",
           "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view",
           "type": "function"},
          {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
           "stateMutability": "view", "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "tokenByIndex",
           "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view",
           "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"},
                                            {"internalType": "uint256", "name": "index", "type": "uint256"}],
                                 "name": "tokenOfOwnerByIndex",
                                 "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                                 "stateMutability": "view", "type": "function"},
          {"inputs": [{"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "tokenURI",
           "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view",
           "type": "function"},
          {"inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
           "stateMutability": "view", "type": "function"}, {
              "inputs": [{"internalType": "address", "name": "from", "type": "address"},
                         {"internalType": "address", "name": "to", "type": "address"},
                         {"internalType": "uint256", "name": "tokenId", "type": "uint256"}], "name": "transferFrom",
              "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}], "name": "transferOwnership",
           "outputs": [], "stateMutability": "nonpayable", "type": "function"},
          {"inputs": [], "name": "withdrawMoney", "outputs": [], "stateMutability": "nonpayable", "type": "function"}]

ck_contract = w3.eth.contract(address=w3.toChecksumAddress(az_token_addr), abi=az_abi)
name = ck_contract.functions.name().call()
symbol = ck_contract.functions.symbol().call()

print(f"{name} {symbol}")


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

logs1 = w3.eth.get_logs({
    "fromBlock": w3.eth.blockNumber - 50000,
    "address": w3.toChecksumAddress(az_token_addr),
    "topics": [event_signature]
})

recent_tx = [get_event_data(w3.codec, transfer_az_abi, log)["args"] for log in logs1]

for tx in recent_tx:
    print(tx["from"], tx["to"], tx['tokenId'])


event_signature2 = w3.sha3(text="transferOwnership(address,address)").hex()

logs2 = w3.eth.get_logs({
    "fromBlock": w3.eth.blockNumber - 500,
    "address": w3.toChecksumAddress(az_token_addr),
    "topics": [event_signature2]
})


ownership_transfer_tx = [get_event_data(w3.codec, ownership_transfer_az_abi, log)["args"] for log in logs2]
print("Ownership transfer")
for tx in ownership_transfer_tx:
    print(tx["previousOwner"], tx["newOwner"])
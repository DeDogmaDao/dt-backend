from web3 import Web3

infura_addr = "https://mainnet.infura.io/v3/9317e901ece9489c8fa9b44078283316"

def get_block_and_save(block_number=None):
    web3_client = Web3(Web3.HTTPProvider(infura_addr))
    if not block_number:
        latest_block = web3_client.eth.get_block('latest')
    else:
        latest_block = web3_client.eth.get_block(block_number)
    with open('blocks.txt', 'a') as f:
        f.write(str(latest_block.number) + ',' + web3_client.toHex(latest_block.hash) + '\n')
    return latest_block.number

block_number = get_block_and_save()
for i in range(1, 10_001):
    get_block_and_save(block_number - i)
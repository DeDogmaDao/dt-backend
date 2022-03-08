import json
import hashlib
from matrix_utils.configs import Config


class Suffle:
    def __init__(self) -> None:
        self.nft_collection_file = 'nft_collection.json'
        self.is_enhance_file = f'{Config.IS_ENHANCE}.json'
        self.all_cards_number = Config.TOTAL_NFTS + Config.ENHANCE_COUNT
    # collection = []
    def load_file(self):
        # open collection
        collection = open(Config.NFT_DATA_DIR + self.nft_collection_file, 'r')
        collection_data = json.load(collection)
        # open enhancers
        # add enhancers at end(doubling enhances)
        enhancers = open(Config.NFT_DATA_DIR + self.is_enhance_file, 'r')
        enhancers_data = json.load(enhancers)
        collection_data.extend(enhancers_data)
        return collection_data

    def randomize(self, block_hash):
        collection = self.load_file()
        hash_to_num = int(block_hash, 16)
        starter = hash_to_num % self.all_cards_number


        nft_places = {}

        for i in range(1, self.all_cards_number+1):
            hash_combined_to_num = block_hash + format(i, 'x')
            hash_of_hash = hashlib.sha512(hash_combined_to_num.encode()).hexdigest()
            nft_places[hash_of_hash] = i
        sorted_keys = sorted(nft_places)
        for idx, item in enumerate(sorted_keys):
            collection[idx], collection[nft_places[item]-1] = collection[nft_places[item]-1], collection[idx]
        return starter, collection


# starter2, sorted_list2 = randomize(block_hash2)
# print(check_colided_places(sorted_list1, sorted_list2))

# collection = load_file()
# print(len(collection))
# Magnet - common - Magnet -> 2 winner , half of reward

# of winner is Magnet, side magnets won't get a chance


# magnets turns on 2 rounds , if one of them get hitted

###################################################

# breaker = 10
# double = 200
# magnet = 100
# enhance = 150
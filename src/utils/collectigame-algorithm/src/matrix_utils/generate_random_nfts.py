import os
import json
from matrix_utils.configs import Config
from random import choice, randint, shuffle


class GenerateRandomNFT:
    
    def __init__(self) -> None:

        self.random_cards = []
        if not os.path.exists(Config.NFT_DATA_DIR):
            os.makedirs(Config.NFT_DATA_DIR)

    def open_and_create_file(self, data, file_name=None, custom_filename=None):
        if not custom_filename:
            f = open(Config.NFT_DATA_DIR+file_name+".json", 'w')
        else:
            f = open(Config.NFT_DATA_DIR+custom_filename, 'w')
        json.dump(data, f, indent=4)
        f.close()

    def create_random_list(self):
        range_1_5000 = list(range(1, Config.TOTAL_NFTS + 1))
        counters_list = []
        for item in Config.COUNTERS_PERCENT:
            (k,v), = item.items()
            for i in range(v):
                counters_list.append(k)
        shuffle(counters_list)
        while len(range_1_5000):
            choosen_random = choice(range_1_5000)
            self.random_cards.append(
                {
                    "card_number": choosen_random,
                    "properties":{
                        "sum": randint(1, 100),
                        "mul": randint(1, 9),
                        "counter": choice(counters_list)
                    }
                },
            )
            range_1_5000.remove(choosen_random)
        return self.random_cards

    def set_rare_cards(self, number_of_rare_cards, cards_list, property):
        rare_list = []
        for i in range(number_of_rare_cards):
            choosen_random = choice(cards_list)
            self.random_cards[choosen_random-1]['properties'][property] = True
            rare_list.append(self.random_cards[choosen_random-1])
            cards_list.remove(choosen_random)
        return rare_list


    def generate_random_nfts(self):
        random_cards = self.create_random_list()

        range_1_5000 = list(range(1, Config.TOTAL_NFTS + 1))
        for card in Config.SPECIAL_CARDS.keys():
            special_cards = self.set_rare_cards(Config.SPECIAL_CARDS[card], range_1_5000, card) 
            self.open_and_create_file(special_cards, file_name=card)

        self.open_and_create_file(random_cards, custom_filename='nft_collection.json')
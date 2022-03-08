import os
import json
from matrix_utils.shuffle import Suffle
from matrix_utils.play_lottery import PlayLottery
from matrix_utils.generate_random_nfts import GenerateRandomNFT

def run_simulator(block_hash, re_generate_nfts=False, store_shuffled_in_file=False):
    if re_generate_nfts:
        # Generate Random NFTs
        generator = GenerateRandomNFT()
        random_cards = generator.create_random_list()

        range_1_5000 = list(range(1, 5001))
        breaker_cards = generator.get_rare_cards(generator.BREAKERS_COUNT, range_1_5000, generator.IS_BREAKER) 
        generator.open_and_create_file(breaker_cards, file_name=generator.IS_BREAKER)

        double_cards = generator.get_rare_cards(generator.DOUBLES_COUNT, range_1_5000, generator.IS_DOUBLER)
        generator.open_and_create_file(double_cards, file_name=generator.IS_DOUBLER)

        magnet_cards = generator.get_rare_cards(generator.MAGNET_COUNT, range_1_5000, generator.IS_MAGNET)
        generator.open_and_create_file(magnet_cards, file_name=generator.IS_MAGNET)

        enhance_cards = generator.get_rare_cards(generator.ENHANCE_COUNT, range_1_5000, generator.IS_ENHANCE)
        generator.open_and_create_file(enhance_cards, file_name=generator.IS_ENHANCE)


        generator.open_and_create_file(random_cards, custom_filename='nft_collection.json')
    # Shuffle them by hash
    suffle = Suffle()
    starter, collection = suffle.randomize(block_hash)
    if store_shuffled_in_file:
        if not os.path.exists("game_data/"):
            os.makedirs("game_data")
        f = open('game_data/suffled_nft_collection.json', 'w')
        json.dump({"collection": collection, "starter": starter}, f, indent=4)
        f.close()
        play_lottery = PlayLottery()
        return play_lottery.play()
    else:
        data = {"collection": collection, "starter": starter}
        play_lottery = PlayLottery()
        return play_lottery.play(data)



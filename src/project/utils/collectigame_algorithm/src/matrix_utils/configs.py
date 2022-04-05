class Config:
    IS_BREAKER = "counter_breaker"
    IS_DOUBLER = "double_counter"
    IS_MAGNET = "magnet"
    IS_ENHANCE = "enhancer"
    BREAKERS_COUNT = 10
    DOUBLES_COUNT = 300
    MAGNET_COUNT = 400
    ENHANCE_COUNT = 250

    SPECIAL_CARDS = {
        IS_BREAKER: BREAKERS_COUNT,
        IS_DOUBLER: DOUBLES_COUNT,
        IS_MAGNET: MAGNET_COUNT,
        IS_ENHANCE: ENHANCE_COUNT
    }
    
    RE_GENERATE_NFTS = False
    STORE_SHUFFLED_IN_FILE = False
    GAME_DATA_DIR = 'game_data/'
    NFT_DATA_DIR = "nft_data/"
    TOTAL_NFTS = 5000
    COUNTERS_PERCENT = [
            {3 : int(TOTAL_NFTS * 0.05)},
            {2 : int(TOTAL_NFTS * 0.1)},
            {1 : int(TOTAL_NFTS * 0.15)},
            {-1 : int(TOTAL_NFTS * 0.25)},
            {-2 : int(TOTAL_NFTS * 0.25)},
            {-3 : int(TOTAL_NFTS * 0.2)},
        ]
    MAGNET_EFFECTIVE_ROUNDS = 3
    ALL_ROUNDS = 50
    STORE_GAME_PROCESS = False
    TOTAL_BLOCKS = 2000
    BASE_WILL_COUNTER = 5
    BASE_TALENT_COUNTER = 0

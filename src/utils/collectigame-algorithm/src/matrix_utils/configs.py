class Config:
    IS_BREAKER = "is_breaker"
    IS_DOUBLER = "is_double"
    IS_MAGNET = "is_magnet"
    IS_ENHANCE = "is_enhance"
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
    STORE_GAME_PROCCESS = False
    TOTAL_BLOCKS = 2000
    BASE_COUNTER = 5
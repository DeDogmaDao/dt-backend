import sys
from collections import defaultdict
import multiprocessing
from test_matrix.simulator import run_simulator
from matrix_utils.configs import Config
from matrix_utils.generate_random_nfts import GenerateRandomNFT


def run_loop(blocks, return_dict):
    for idx, block in enumerate(blocks):
        print(idx)
        _block_num, block_hash = block.split(',')
        block_hash = block_hash.replace('\n', '')
        _winners, nfts, round, magnet_is_on, magnet_stole = run_simulator(block_hash)
        for item in nfts:
            if item['properties'].get('is_breaker'):
                return_dict["counter_breakers"] += 1
            elif item['properties'].get('is_double'):
                return_dict["doublers"] += 1
            elif item['properties'].get('is_enhance'):
                return_dict["enhancer"] += 1
            elif item['properties'].get('is_magnet'):
                return_dict["magnet"] += 1
            else:
                return_dict["common"] += 1
            
            if round == Config.ALL_ROUNDS+1:
                return_dict[f"round{Config.ALL_ROUNDS+1}"] += 1
            if magnet_is_on:
                return_dict["magnet_was_on"] += 1
            if magnet_stole:
                return_dict["magnet_stole"] += 1
    return return_dict

def get_result(GLOBAL_STATS, TOTAL_BLOCKS):
    print(GLOBAL_STATS)
    breaker_ratio = Config.BREAKERS_COUNT/Config.TOTAL_NFTS
    double_ratio = Config.DOUBLES_COUNT/Config.TOTAL_NFTS
    magnet_ratio = Config.MAGNET_COUNT/Config.TOTAL_NFTS
    enhance_ratio = Config.ENHANCE_COUNT/Config.TOTAL_NFTS
    common_ratio = (Config.TOTAL_NFTS -(
        Config.ENHANCE_COUNT +
        Config.BREAKERS_COUNT +
        Config.DOUBLES_COUNT +
        Config.MAGNET_COUNT
        ))/Config.TOTAL_NFTS
    print("### BREAKERS ratio:" + f"{breaker_ratio:.5f}")
    print("### DOUBLES ratio:" + f"{double_ratio:.5f}")
    print("### MAGNET ratio:" + f"{magnet_ratio:.5f}")
    print("### ENHANCE ratio:" + f"{enhance_ratio:.5f}")
    print("### COMMON ratio:" + f"{common_ratio:.5f}")
    print("------------------------------------------------------")
    breaker_win_ratio = GLOBAL_STATS.get('counter_breakers')/TOTAL_BLOCKS
    double_win_ratio = GLOBAL_STATS.get('doublers')/TOTAL_BLOCKS
    magnet_win_ratio = GLOBAL_STATS.get('magnet')/TOTAL_BLOCKS
    enhance_win_ratio = GLOBAL_STATS.get('enhancer')/TOTAL_BLOCKS
    common_win_ratio = GLOBAL_STATS.get('common')/TOTAL_BLOCKS
    print("** BREAKERS win ratio:" + f"{breaker_win_ratio:.5f}")
    print("** DOUBLES win ratio:" + f"{double_win_ratio:.5f}")
    print("** MAGNET win ratio:" + f"{magnet_win_ratio:.5f}")
    print("** ENHANCE win ratio:" + f"{enhance_win_ratio:.5f}")
    print("** COMMON win ratio:" + f"{common_win_ratio:.5f}")
    print("------------------------------------------------------")
    print("** BREAKERS win coefficient:" + f"{(breaker_win_ratio/breaker_ratio):.5f}")
    print("** DOUBLES win coefficient:" + f"{(double_win_ratio/double_ratio):.5f}")
    print("** MAGNET win coefficient:" + f"{(magnet_win_ratio/magnet_ratio):.5f}")
    print("** ENHANCE win coefficient:" + f"{(enhance_win_ratio/enhance_ratio):.5f}")
    print("** COMMON win coefficient:" + f"{(common_win_ratio/common_ratio):.5f}")

if __name__ == "__main__":

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    return_dict["counter_breakers"] = 0
    return_dict["doublers"] = 0
    return_dict["enhancer"] = 0
    return_dict["magnet"] = 0
    return_dict["common"] = 0
    return_dict[f"round{Config.ALL_ROUNDS+1}"] = 0
    return_dict["magnet_was_on"] = 0
    return_dict["magnet_stole"] = 0
    ############
    command = ""
    if len(sys.argv) > 1:
        command = sys.argv[1]
    if command == "generate":
        random_nfts = GenerateRandomNFT()
        random_nfts.generate_random_nfts()
        print("### Generated ###")
    elif command == "par":
        f = open('10k_prev_blocks.txt', 'r')
        blocks = f.readlines()
        f.close()
        jobs = []
        for i in range(4):
            p = multiprocessing.Process(target=run_loop, args=(blocks[500*i:(500*i)+500], return_dict))
            jobs.append(p)
        for job in jobs: job.start()
        for job in jobs: job.join()
        print("return_dict", return_dict)
        get_result(return_dict, 2_000)
    else:
        f = open('10k_prev_blocks.txt', 'r')
        blocks = f.readlines()
        f.close()
        return_dict = defaultdict(int)
        run_loop(blocks[:Config.TOTAL_BLOCKS], return_dict)
        print("return_dict", return_dict)
        get_result(return_dict, Config.TOTAL_BLOCKS)

        
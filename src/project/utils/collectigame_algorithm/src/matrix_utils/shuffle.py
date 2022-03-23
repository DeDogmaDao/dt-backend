import hashlib


class Suffle:
    def __init__(self, card_numbers) -> None:
        self.card_numbers = card_numbers

    def randomize(self, block_hash):
        hash_to_num = int(block_hash, 16)
        starter = hash_to_num % self.card_numbers


        nft_places = {}

        for i in range(1, self.card_numbers+1):
            hash_combined_to_num = block_hash + format(i, 'x')
            hash_of_hash = hashlib.sha512(hash_combined_to_num.encode()).hexdigest()
            nft_places[hash_of_hash] = i
        sorted_keys = sorted(nft_places)
        sorted_dict = {}
        for i in sorted_keys:
            sorted_dict[i] = nft_places[i]
        return starter, sorted_dict

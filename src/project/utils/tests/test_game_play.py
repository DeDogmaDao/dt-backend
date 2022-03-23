from random import choice
from django.test import TestCase
from project.round.models import Round
from project.nft.models import NFT, FullDeck, ChosenCard
from project.utils.collectigame_algorithm.src.matrix_utils.generate_random_nfts import GenerateRandomNFT
from project.utils.collectigame_algorithm.src.matrix_utils.shuffle import Suffle
from project.utils.collectigame_algorithm.src.matrix_utils.play_lottery import PlayLottery
from project.nft.enums import BloodType, Rarity, CounterType, Side


class GameTestCase(TestCase):
    def setUp(self):
        nft = []
        nft_obj = GenerateRandomNFT()
        r_nfts = nft_obj.generate_random_nfts()
        blood_types = [BloodType.ZEUS,
                       BloodType.POSEIDON,
                       BloodType.HADES,
                       BloodType.HESTIA,
                       BloodType.HERA,
                       BloodType.APHRODITE,
                       BloodType.ARTEMIS,
                       BloodType.ATENA,
                       BloodType.ARES,
                       BloodType.HERMES]
        for idx, item in enumerate(r_nfts):
            blood = choice(blood_types)
            nft.append(
                NFT(
                    token_id=idx+1,
                    image_2d="img2d",
                    image_3d="img3d",
                    speciality=item['properties']['counter_type'],
                    counter=item['properties']['counter'],
                    side=item['properties']['side'],
                    multiply_num=item['properties']['mul'],
                    sum_num=item['properties']['sum'],
                    rarity=Rarity.GOD if item['properties']['counter_type'] ==
                                         CounterType.COUNTER_BREAKER else Rarity.COMMON,
                    blood=blood,
                    blood_portion=1 if blood == BloodType.ZEUS else 0,
                    is_upgraded=False
                )

            )
        NFT.objects.bulk_create(nft)
        eth_block = "0xe890dbf5ee13f4f43d6777b5afcb5e8913af15ea3d8eb9dc6cb03852df8b147c"
        self.round = Round.objects.create_round(66.66, eth_block)

        shuffle_obj = Suffle(5000)
        shuffled_obj = shuffle_obj.randomize(eth_block)
        deck = []
        starter, sorted_dict = shuffled_obj
        for i,(k,v) in enumerate(sorted_dict.items()):
            deck.append(FullDeck(
                nft_id=i+1,
                round=self.round,
                deck_place=v,
                wallet="0xwallet" + str(i+1)
            ))
        FullDeck.objects.bulk_create(deck)

    def test_animals_can_speak(self):
        print("HELL finally?")
        self.assertEqual(1, 1)
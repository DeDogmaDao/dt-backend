from random import choice
from django.test import TestCase
from project.round.models import Round
from project.nft.models import NFT, FullDeck, ChosenCard
from project.utils.collectigame_algorithm.src.matrix_utils.generate_random_nfts import GenerateRandomNFT
from project.utils.collectigame_algorithm.src.matrix_utils.shuffle import Suffle
from project.utils.collectigame_algorithm.src.matrix_utils.play_lottery import PlayLottery
from project.nft.enums import BloodType, Rarity, CounterType


class GameTestCase(TestCase):
    def setUp(self):
        self.generate_random_nfts()

    def generate_random_nfts(self):
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
        self.eth_block = "0xe890dbf5ee13f4f43d6777b5afcb5e8913af15ea3d8eb9dc6cb03852df8b147c"
        self.round = Round.objects.create_round(66.66, self.eth_block)

        self.shuffle_obj = Suffle(5000)
        shuffled_obj = self.shuffle_obj.randomize(self.eth_block)
        deck = []
        starter, sorted_dict = shuffled_obj
        # print(starter)
        for i,(k,v) in enumerate(sorted_dict.items()):
            deck.append(FullDeck(
                nft_id=i+1,
                round=self.round,
                deck_place=v,
                wallet="0xwallet" + str(i+1),
                is_starter=True if v == starter else False
            ))
        FullDeck.objects.bulk_create(deck)
        self.starter = FullDeck.objects.get(is_starter=True, round=self.round)
        self.starter_deck_place = self.starter.deck_place

        full_deck = FullDeck.objects.filter(round=self.round).select_related("nft")
        lottery = PlayLottery(full_deck, self.starter_deck_place)
        self.winners, self.chosen_cards = lottery.play()
        self.chosen_card_list = [ChosenCard(**card, round=self.round) for card in self.chosen_cards]
        ChosenCard.objects.bulk_create(self.chosen_card_list)
        # print(self.starter)

    def test_can_play_game(self):
        self.assertGreater(len(self.winners), 0)

from django.test import TestCase
from project.nft.models import NFT


class GameTestCase(TestCase):
    def setUp(self):
        NFT.objecs.bulk_create(

        )

    def test_animals_can_speak(self):
        print("HELL finally?")
        self.assertEqual(1, 1)
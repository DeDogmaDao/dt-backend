from rest_framework import serializers
from project.nft.models import NFT, FullDeck


class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = '__all__'


class FullDeckSerializer(serializers.ModelSerializer):
    nft = NFTSerializer()
    class Meta:
        model = FullDeck
        fields = '__all__'

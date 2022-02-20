from django.contrib import admin

from .chosen_card import ChosenCardAdmin
from .full_deck import FullDeckAdmin
from .nft import NFTAdmin


from nft.models import ChosenCard, FullDeck, NFT

admin.site.register(ChosenCard, ChosenCardAdmin)
admin.site.register(FullDeck, FullDeckAdmin)
admin.site.register(NFT, NFTAdmin)

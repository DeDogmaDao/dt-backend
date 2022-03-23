from django.db import models
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class FullDeck(BaseModel):
    nft = models.ForeignKey(
        verbose_name=_("NFT"),
        to="nft.NFT",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    round = models.ForeignKey(
        verbose_name=_("Round"),
        to="round.Round",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    deck_place = models.PositiveIntegerField(
        verbose_name=_("Deck place")
    )
    wallet = models.CharField(
        verbose_name=_("Deck place"),
        max_length=1024
    )
    #
    # class Meta:
    #     app_label = "full_deck"

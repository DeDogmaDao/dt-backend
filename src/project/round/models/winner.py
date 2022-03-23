from django.db import models
from project.nft.enums import Rarity
from project.utils.base_model import BaseModel
from project.round.enums import FulfillStatus
from django.utils.translation import gettext_lazy as _


class Winner(BaseModel):
    round = models.ForeignKey(
        to="round.Round",
        verbose_name=_("Round"),
        related_name="round_winners",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    winner_wallet = models.CharField(
        verbose_name=_("Winner wallet"),
        max_length=1024,
    )
    winner_nft = models.ForeignKey(
        verbose_name=_("Winner nft"),
        to="nft.NFT",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    transaction = models.ForeignKey(
        to="blockchain_transaction.Transaction",
        verbose_name=_("Transaction"),
        related_name="winners",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fulfill_status = models.CharField(
        choices=FulfillStatus.CHOICES,
        max_length=100
    )
    is_original_winner = models.BooleanField(
        verbose_name=_("Is original winner")
    )
    winner_type = models.CharField(
        verbose_name=_("Winner type"),
        max_length=100,
        choices=Rarity.CHOICES
    )
    winner_portion = models.DecimalField(
        verbose_name=_("Winner portion"),
        decimal_places=2,
        max_digits=30
    )


from django.db import models
from round.enums import DaysEnum
from utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class Round(BaseModel):
    week_num = models.PositiveIntegerField(
        verbose_name=_("Week number"),
    )
    day = models.CharField(
        verbose_name=_("Day"),
        max_length=60,
        choices=DaysEnum.CHOICES
    )
    game_num = models.PositiveIntegerField(
        verbose_name=_("Game number"),
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
    winner_prize = models.PositiveIntegerField(
        verbose_name=_("Winner prize"),
    )
    eth_block_number = models.CharField(
        verbose_name=_("Eth block number"),
        max_length=1024,
    )
    finished = models.BooleanField(
        verbose_name=_("Finished"),
        default=False
    )

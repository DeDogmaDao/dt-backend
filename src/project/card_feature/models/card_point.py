from django.db import models
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class CardPoint(BaseModel):
    nft = models.ForeignKey(
        verbose_name=_("NFT"),
        to="nft.NFT",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    chosen_counts = models.PositiveIntegerField(
        verbose_name=_("Chosen")
    )
    allow_upgrade = models.BooleanField(
        verbose_name=_("Allow upgrade"),
        default=False
    )

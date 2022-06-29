from django.db import models

from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class Profile(BaseModel):
    nft = models.ManyToManyField(
        verbose_name=_("NFT"),
        to="nft.NFT",
    )
    wallet = models.CharField(
        verbose_name=_("Wallet"),
        max_length=1024
    )
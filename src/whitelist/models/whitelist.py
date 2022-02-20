from django.db import models
from utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class Whitelist(BaseModel):
    nonce = models.PositiveIntegerField(
        verbose_name=_("nonce"),
    )
    max_allowed_mint = models.PositiveIntegerField(
        verbose_name=_("Max allowed mint")
    )
    wallet = models.CharField(
        verbose_name=_("Wallet"),
        max_length=1024
    )
    signed_message = models.CharField(
        verbose_name=_("Signed message"),
        max_length=1024
    )

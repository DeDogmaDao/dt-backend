from django.db import models
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class TransferHistory(BaseModel):
    block_number = models.CharField(
        max_length=512,
        verbose_name=_("Block number")
    )
    from_address = models.CharField(
        max_length=1024,
        verbose_name=_("From address")
    )
    from_ens = models.CharField(
        max_length=1024,
        verbose_name=_("From ENS"),
        null=True,
        blank=True
    )
    to_address = models.CharField(
        max_length=1024,
        verbose_name=_("To address")
    )
    to_ens = models.CharField(
        max_length=1024,
        verbose_name=_("To ENS"),
        null=True,
        blank=True
    )
    tx_hash = models.CharField(
        max_length=1024,
        verbose_name=_("Transaction hash")
    )
    token_id = models.PositiveIntegerField(
        verbose_name=_("Token id")
    )
    timestamp = models.DateTimeField(
        verbose_name=_("Timestamp")
    )
    analyzed = models.BooleanField(
        verbose_name=_("Analyzed"),
        default=False
    )

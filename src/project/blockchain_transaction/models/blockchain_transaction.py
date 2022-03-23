from django.db import models
from project.blockchain_transaction.enums import TransactionStatus, TransactionType
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class Transaction(BaseModel):
    from_wallet = models.CharField(
        verbose_name=_("From wallet"),
        max_length=1024,
    )
    to_wallet = models.CharField(
        verbose_name=_("To wallet"),
        max_length=1024,
    )
    amount = models.DecimalField(
        verbose_name=_("Amount"),
        decimal_places=2,
        max_digits=30
    )
    unit = models.CharField(
        verbose_name=_("Unit"),
        max_length=1024,
    )
    transaction_type = models.CharField(
        verbose_name=_("Transaction type"),
        max_length=100,
        choices=TransactionType.CHOICES
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=100,
        choices=TransactionStatus.CHOICES
    )
    is_multi_sig = models.BooleanField(
        verbose_name=_("Is multi sig"),
    )
    tx_id = models.CharField(
        verbose_name=_("Tx id"),
        max_length=1024
    )

from django.db import models
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class ChosenCard(BaseModel):
    deck_place = models.ForeignKey(
        verbose_name=_("Deck place"),
        to="nft.FullDeck",
        related_name="chosen_cards",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    total_counter = models.PositiveIntegerField(
        verbose_name=_("Total counter"),
        null=True
    )
    magnet_status = models.BooleanField(
        verbose_name=_("Magnet status"),
        default=False
    )

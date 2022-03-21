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

    # class Meta:
    #     app_label = "chosen_card"

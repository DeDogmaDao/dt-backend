from django.db import models
from project.nft.enums import BloodType, Rarity, CounterType, Side
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class NFT(BaseModel):
    token_id = models.PositiveIntegerField(
        verbose_name=_("Token id")
    )
    image_2d = models.ImageField(
        verbose_name=_("Image 2d"),
        null=True,
        blank=True
    )
    image_3d = models.ImageField(
        verbose_name=_("Image 3d"),
        null=True,
        blank=True
    )
    speciality = models.CharField(
        verbose_name=_("Speciality"),
        max_length=32,
        choices=CounterType.CHOICES,
        null=True,
        blank=True
    )
    counter = models.PositiveIntegerField(
        verbose_name=_("Counter"),
        null=True,
        blank=True
    )
    side = models.CharField(
        verbose_name=_("Side"),
        max_length=100,
        choices=Side.CHOICES,
        null=True,
        blank=True
    )
    multiply_num = models.PositiveIntegerField(
        verbose_name=_("Multiply number"),
        null=True,
        blank=True
    )
    sum_num = models.PositiveIntegerField(
        verbose_name=_("Sum number"),
        null=True,
        blank=True
    )
    rarity = models.CharField(
        verbose_name=_("Rarity"),
        max_length=32,
        choices=Rarity.CHOICES,
        null=True,
        blank=True
    )
    blood = models.CharField(
        verbose_name=_("Blood"),
        max_length=32,
        choices=BloodType.CHOICES,
        null=True,
        blank=True
    )
    blood_portion = models.PositiveIntegerField(
        verbose_name=_("Blood portion"),
        null=True,
        blank=True
    )
    is_upgraded = models.BooleanField(
        verbose_name=_("Is upgraded"),
        default=False
    )
    is_revealed = models.BooleanField(
        verbose_name=_("Is revealed"),
        default=False
    )
    #
    # class Meta:
    #     app_label = "nft"

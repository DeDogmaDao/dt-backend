from django.db import models
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class ScannerState(BaseModel):
    last_scanned_block = models.PositiveBigIntegerField(
        verbose_name=_("Last scanned block")
    )
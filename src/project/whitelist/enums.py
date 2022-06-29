from django.utils.translation import gettext_lazy as _


class WhiteListType:
    ROYAL = "royal" # 1
    COMMON = "common" # 0

    CHOICES = [
        (
            ROYAL, _("Royal")
        ),
        (
            COMMON, _("Common")
        ),
    ]

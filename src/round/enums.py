from django.utils.translation import gettext_lazy as _

class DaysEnum:
    DAY_ONE = "day_one"
    DAY_TWO = "day_two"
    DAY_THREE = "day_three"
    DAY_FOUR = "day_four"
    DAY_FIVE = "day_five"
    DAY_SIX = "day_six"
    DAY_SEVEN = "day_seven"

    CHOICES = [
        (
            DAY_ONE, _("Day one")
        ),
        (
            DAY_TWO, _("Day two")
        ),
        (
            DAY_THREE, _("Day three")
        ),
        (
            DAY_FOUR, _("Day four")
        ),
        (
            DAY_FIVE, _("Day five")
        ),
        (
            DAY_SIX, _("Day six")
        ),
        (
            DAY_SEVEN, _("Day seven")
        )
    ]
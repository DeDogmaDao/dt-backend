from django.utils.translation import gettext_lazy as _

class BloodType:
    ZEUS = "zeos"

    CHOICES = [
        (
            ZEUS, _("Zeos")
        ),
    ]

class CounterType:
    ENHANCER = "enhancer"
    DOUBLE_COUNTER = "double_counter"
    MAGNET = "magnet"
    COUNTER_BREAKER = "counter_breaker"

    CHOICES = [
        (
            ENHANCER, _("Enhancer")
        ),
        (
            DOUBLE_COUNTER, _("Double counter")
        ),
        (
            MAGNET, _("Magnet")
        ),
        (
            COUNTER_BREAKER, _("Counter breaker")
        ),
    ]

class Rarity:
    COMMON = "common"
    GOD = "god"

    CHOICES = [
        (
            COMMON, _("Common")
        ),
        (
            GOD, _("God")
        ),
    ]

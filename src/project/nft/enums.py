from django.utils.translation import gettext_lazy as _

class BloodType:
    ZEUS = "zeos"
    POSEIDON = "poseidon"
    HADES = "hades"
    HESTIA = "hestia"
    HERA = "hera"
    APHRODITE = "aphrodite"
    ARTEMIS = "artemis"
    ATENA = "atena"
    ARES = "ares"
    HERMES = "hermes"

    CHOICES = [
        (
            ZEUS, _("Zeos")
        ),
        (
            POSEIDON, _("Poseidon")
        ),
        (
            HADES, _("Hades")
        ),
        (
            HESTIA, _("Hestia")
        ),
        (
            HERA, _("Hera")
        ),
        (
            APHRODITE, _("Aphrodite")
        ),
        (
            ATENA, _("Atena")
        ),
        (
            ARES, _("Ares")
        ),
        (
            HERMES, _("Hermes")
        ),
    ]

class CounterType:
    ENHANCER = "enhancer"
    DOUBLE_COUNTER = "double_counter"
    MAGNET = "magnet"
    COUNTER_BREAKER = "counter_breaker"
    SPECIAL_DROP = "special_drop"
    NOTHING = "nothing"

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
        (
            SPECIAL_DROP, _("Special drop")
        ),
        (
            NOTHING, _("Nothing")
        )
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


class Side:
    WILL = "will"
    TALENT = "talent"

    CHOICES = [
        (
            WILL, _("Will")
        ),
        (
            TALENT, _("Talent")
        ),
    ]
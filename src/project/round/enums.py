from django.utils.translation import gettext_lazy as _


class FulfillStatus:
    FULFILLED = "fulfilled"
    UNFULFILLED = "unfulfilled"
    PARTIALLY_FULFILLED = "partially_fulfilled"

    CHOICES = [
        (
            FULFILLED, _("Fulfilled")
        ),
        (
            UNFULFILLED, _("Unfulfilled")
        ),
        (
            PARTIALLY_FULFILLED, _("Partially fulfilled")
        ),
    ]


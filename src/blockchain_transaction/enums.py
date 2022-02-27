from django.utils.translation import gettext_lazy as _


class TransactionType:
    SEND_MONEY = "send_money"
    SEND_MESSAGE = "send_message"

    CHOICES = [
        (
            SEND_MONEY, _("Send money")
        ),
        (
            SEND_MESSAGE, _("Send message")
        ),
    ]


class TransactionStatus:
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    PENDING = "pending"

    CHOICES = [
        (
            SUCCEEDED, _("Succeeded"),
        ),
        (
            FAILED, _("Failed"),
        ),
        (
            PENDING, _("Pending")
        )
    ]

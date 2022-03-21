from django.contrib.admin import ModelAdmin, display


class ChosenCardAdmin(ModelAdmin):
    list_display = ["id", "wallet"]

    @display(description='Wallet')
    def wallet(self, obj):
        return obj.full_deck.wallet

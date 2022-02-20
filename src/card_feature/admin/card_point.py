from django.contrib.admin import ModelAdmin, display


class CardPointAdmin(ModelAdmin):
    list_display = ["id", "token_id", "chosen_counts", "allow_upgrade"]

    @display(description="Get nft")
    def token_id(self, obj):
        return obj.nft.token_id

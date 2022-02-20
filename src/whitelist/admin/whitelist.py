from django.contrib.admin import ModelAdmin


class WhitelistAdmin(ModelAdmin):
    list_display = ["id", "max_allowed_mint", "wallet"]

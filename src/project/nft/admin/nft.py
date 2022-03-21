from django.contrib.admin import ModelAdmin


class NFTAdmin(ModelAdmin):
    list_display = ["id", "token_id", "speciality", "counter", "rarity", "blood"]

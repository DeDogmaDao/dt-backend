from django.contrib.admin import ModelAdmin


class FullDeckAdmin(ModelAdmin):
    list_display = ["id", "deck_place", "wallet"]

from django.contrib.admin import ModelAdmin


class RoundAdmin(ModelAdmin):
    list_display = ["id", "week_num", "day", "game_num"]

from django.contrib.admin import ModelAdmin


class ScannerStateAdmin(ModelAdmin):
    list_display = ["id", "last_scanned_block"]

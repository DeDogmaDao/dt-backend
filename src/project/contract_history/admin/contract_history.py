from django.contrib.admin import ModelAdmin


class ContractHistoryAdmin(ModelAdmin):
    list_display = ["id", "block_number", "from_address", "to_address"]

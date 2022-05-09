from django.contrib import admin

from .contract_history import ContractHistoryAdmin
from project.contract_history.models import TransferHistory

admin.site.register(TransferHistory, ContractHistoryAdmin)

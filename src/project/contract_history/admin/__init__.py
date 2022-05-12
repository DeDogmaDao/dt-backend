from django.contrib import admin

from .contract_history import ContractHistoryAdmin
from .scanner_state import ScannerStateAdmin
from project.contract_history.models import TransferHistory, ScannerState

admin.site.register(TransferHistory, ContractHistoryAdmin)
admin.site.register(ScannerState, ScannerStateAdmin)

from celery.utils.log import get_task_logger

from project import celery_app
from project.utils.base_task import BaseTask

from project.utils.blockchain_event_scanner_v2 import Scanner


class FetchContractHistoryTask(BaseTask):
    name = 'project.contract_history.tasks.FetchContractHistoryTask'
    logger = get_task_logger(__name__)

    def _run(self, *args, **kwargs):
        scanner = Scanner()
        scanner.run()

celery_app.tasks.register(FetchContractHistoryTask())
celery_app.add_periodic_task(10.0, FetchContractHistoryTask())

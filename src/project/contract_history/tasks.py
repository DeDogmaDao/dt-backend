from celery.utils.log import get_task_logger

from project import celery_app
from project.utils.base_task import BaseTask

from project.utils.blockchain_event_scanner import run_fetch


class FetchContractHistoryTask(BaseTask):
    name = 'project.contract_history.tasks.FetchContractHistoryTask'
    logger = get_task_logger(__name__)

    def _run(self, *args, **kwargs):
        run_fetch(
            "https://mainnet.infura.io/v3/9317e901ece9489c8fa9b44078283316")  # TODO: add infura url into github secrets


celery_app.tasks.register(FetchContractHistoryTask())
celery_app.add_periodic_task(10.0, FetchContractHistoryTask())

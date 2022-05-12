from celery.schedules import crontab
from celery.utils.log import get_task_logger

from project import celery_app
from django.utils import timezone
from project.utils.base_task import BaseTask

from project.utils.blockchain_event_scanner import run_fetch


class FetchContractHistoryTask(BaseTask):
    name = 'project.contract_history.tasks.FetchContractHistoryTask'
    logger = get_task_logger(__name__)

    def _run(self, *args, **kwargs):
        data = self.fetch_data()
        run_fetch("https://mainnet.infura.io/v3/9317e901ece9489c8fa9b44078283316")
        print(data, timezone.now())

    def fetch_data(self):
        return "stupid data"


celery_app.tasks.register(FetchContractHistoryTask())
celery_app.add_periodic_task(5.0, FetchContractHistoryTask())

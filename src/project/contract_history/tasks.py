from celery.schedules import crontab
from celery.utils.log import get_task_logger

from project import celery_app
from django.utils import timezone
from project.utils.base_task import BaseTask


class FetchContractHistoryTask(BaseTask):
    name = 'project.contract_history.tasks.FetchContractHistoryTask'
    logger = get_task_logger(__name__)

    def _run(self, *args, **kwargs):
        data = self.fetch_data()
        print(data, timezone.now())

    def fetch_data(self):
        return "stupid data"


celery_app.tasks.register(FetchContractHistoryTask())
celery_app.add_periodic_task(crontab(minute="*/1"), FetchContractHistoryTask())

from celery.schedules import crontab
from celery.utils.log import get_task_logger

from project import celery_app
from django.utils import timezone
from project.utils.base_task import BaseTask


class FetchNFTDataTask(BaseTask):
    name = 'project.nft.tasks.FetchNFTDataTask'
    logger = get_task_logger(__name__)

    def _run(self, *args, **kwargs):
        data = self.fetch_data()
        print(data, timezone.now())

    def fetch_data(self):
        return "stupid data"


celery_app.tasks.register(FetchNFTDataTask())
celery_app.add_periodic_task(crontab(minute="*/1"), FetchNFTDataTask())

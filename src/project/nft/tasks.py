from celery.utils.log import get_task_logger

from project import celery_app
from django.utils import timezone
from project.utils.base_task import BaseTask

from project.contract_history.models import TransferHistory
from project.nft.models import FullDeck, NFT
from project.round.models import Round


class FillFullDeckTask(BaseTask):
    name = 'project.nft.tasks.FillFullDeckTask'
    logger = get_task_logger(__name__)

    def _run(self, *args, **kwargs):
        self.fill_data()

    def fill_data(self):
        # TODO: aggregate OpenSee Transfers
        try:
            round = Round.objects.get(finished=False)
            transfers = TransferHistory.objects.filter(
                analyzed=False
            ).order_by("id")
            for transfer in transfers:
                nft, _created = NFT.objects.get_or_create(defaults={"token_id": transfer.token_id})
                current_full_deck =FullDeck.objects.filter(round=round).count()
                FullDeck.objects.create(
                    round=round,
                    nft=nft,
                    deck_place=current_full_deck+1,
                    wallet=transfer.to_address
                )
        except Round.DoesNotExist:
            print("No round yet")


celery_app.tasks.register(FillFullDeckTask())
celery_app.add_periodic_task(10.0, FillFullDeckTask())

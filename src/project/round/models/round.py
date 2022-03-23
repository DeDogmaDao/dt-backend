from django.db import models
from project.utils.base_model import BaseModel
from django.utils.translation import gettext_lazy as _

class RoundQuerySet(models.QuerySet):
    def create_round(self, winners_total_prize, eth_block_number):
        try:
            latest = self.latest('created_at')
            day = (latest.day % 7) + 1
            week_num = latest.week_num
            if latest.day == 7:
                week_num = latest.week_num + 1
            game_num = latest.game_num + 1
        except Round.DoesNotExist:
            day = 1
            game_num = 1
            week_num = 1

        return self.create(
            week_num=week_num,
            day=day,
            game_num=game_num,
            winners_total_prize=winners_total_prize,
            eth_block_number=eth_block_number,
            finished=False
        )


class Round(BaseModel):
    week_num = models.PositiveIntegerField(
        verbose_name=_("Week number"),
    )
    day = models.PositiveIntegerField(
        verbose_name=_("Day"),
    )
    game_num = models.PositiveIntegerField(
        verbose_name=_("Game number"),
    )
    winners_total_prize = models.PositiveIntegerField(
        verbose_name=_("Winner prize"),
    )
    eth_block_number = models.CharField(
        verbose_name=_("Eth block number"),
        max_length=1024,
    )
    finished = models.BooleanField(
        verbose_name=_("Finished"),
        default=False
    )
    objects = RoundQuerySet.as_manager()

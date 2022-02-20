from django.contrib import admin

from .round import RoundAdmin
from round.models import Round

admin.site.register(Round, RoundAdmin)

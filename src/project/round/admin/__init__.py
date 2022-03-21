from django.contrib import admin

from .round import RoundAdmin
from project.round.models import Round

admin.site.register(Round, RoundAdmin)

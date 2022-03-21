from django.contrib import admin

from .whitelist import WhitelistAdmin
from project.whitelist.models import Whitelist

admin.site.register(Whitelist, WhitelistAdmin)
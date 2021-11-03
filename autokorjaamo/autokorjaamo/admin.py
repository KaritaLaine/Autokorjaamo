from django.contrib import admin
from .models import *

class PalveluAdmin(admin.ModelAdmin):
    fields = ["palvelu", "hinta"]

admin.site.register(Palvelu,PalveluAdmin)
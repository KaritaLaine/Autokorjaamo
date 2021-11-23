from django.contrib import admin
from .models import *

admin.site.register(Palaute)

admin.site.register(ajanvaraus)

class PalveluAdmin(admin.ModelAdmin):
    fields = ["palvelu", "hinta"]

admin.site.register(Palvelu,PalveluAdmin)
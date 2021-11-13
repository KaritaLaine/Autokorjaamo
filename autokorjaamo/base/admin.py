from django.contrib import admin
from .models import *

admin.site.register(Palaute)

class PalveluAdmin(admin.ModelAdmin):
    fields = ["palvelu", "hinta", "sposti"]

admin.site.register(Palvelu,PalveluAdmin)
from django.db import models

class Palaute(models.Model):
    nimi = models.CharField(max_length=50)
    palaute = models.TextField(max_length=1000)




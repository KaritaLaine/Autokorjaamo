from django.db import models

class Palaute(models.Model):
    nimi = models.CharField(max_length=50)
    palaute = models.TextField(max_length=1000)

class Palvelu(models.Model):
    palvelu = models.CharField(max_length=200)
    hinta = models.CharField(max_length=200)

    def __str__(self):
        return self.palvelu




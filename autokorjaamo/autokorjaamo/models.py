from django.db import models

class Palvelu(models.Model):
    palvelu = models.CharField(max_length=200)
    hinta = models.CharField(max_length=200)

    def __str__(self):
        return self.palvelu
from django.db import models

class Palaute(models.Model):
    nimi = models.CharField(max_length=50)
    palaute = models.TextField(max_length=1000)
    sposti = models.EmailField(max_length=150)

    def __str__(self):
        return self.palaute

class Palvelu(models.Model):
    palvelu = models.CharField(max_length=200)
    hinta = models.CharField(max_length=200)

    def __str__(self):
        return self.palvelu


class ajanvaraus(models.Model):
    nimi = models.CharField(max_length=50)
    sposti = models.EmailField(max_length=150)
    puh = models.CharField(max_length=12)
    osoite = models.CharField(max_length=150)

    rekisterinumero = models.CharField(max_length=10)
    vuosimalli = models.IntegerField()
    merkki = models.CharField(max_length = 20)
    malli = models.CharField(max_length = 150)
    kilometrit = models.IntegerField()
    lisatiedot = models.TextField(max_length=1000)

    pvm = models.DateField(max_length=10)
    klo = models.TimeField(max_length=10)

    def __str__(self):
        return self.ajanvaraus



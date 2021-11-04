from django import forms
from django.forms import ModelForm
from .models import Palaute


class PalauteLomake(ModelForm):
    class Meta:
        model = Palaute
        fields = ('nimi', 'palaute')

        widgets = {
            'nimi': forms.TextInput(attrs={'class':'form-control'})

        }
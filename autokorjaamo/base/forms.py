from django import forms
from django.forms import ModelForm
from .models import Palaute


class PalauteLomake(forms.ModelForm):
    class Meta:
        model = Palaute
        fields = ('nimi', 'palaute')
        labels = {
            'nimi': '',
            'palaute': ''
        }
        widgets = {
            'nimi': forms.TextInput(attrs={'placeholder': 'Nimi...', 'class': 'palaute_nimi'}),
            'palaute': forms.Textarea(attrs={'placeholder': 'Anna palautetta...', 'class': 'palaute_textarea'})
        }
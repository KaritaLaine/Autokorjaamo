from django import forms
from django.forms import ModelForm
from .models import Palaute


class PalauteLomake(forms.ModelForm):
    class Meta:
        model = Palaute
        fields = ('nimi', 'sposti', 'palaute')
        labels = {
            'nimi': '',
            'sposti': '',
            'palaute': ''
        }
        widgets = {
            'nimi': forms.TextInput(attrs={'placeholder': 'Nimi...', 'class': 'palaute_nimi'}),
            'palaute': forms.Textarea(attrs={'placeholder': 'Anna palautetta...', 'class': 'palaute_textarea'}),
            'sposti': forms.EmailInput(attrs={'placeholder': 'Sähköposti...', 'class': 'palaute_sposti'})
        }
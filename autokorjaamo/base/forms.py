from django import forms
from django.forms import ModelForm
from .models import Palaute, ajanvaraus


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


class ajanvaraus(forms.ModelForm):
    class Meta:
        model = ajanvaraus
        fields = ('nimi', 'sposti', 'puh', 'osoite', 'rekisterinumero', 'vuosimalli', 'merkki', 'malli', 'kilometrit', 'lisatiedot', 'pvm', 'klo')
        labels = {
            'nimi': '',
            'sposti': '',
            'puh': '',
            'osoite':'',
            'rekisterinumero':'',
            'vuosimalli':'',
            'merkki':'',
            'malli':'',
            'kilometrit':'',
            'lisatiedot':'',
            'pvm':'',
            'klo':'',
        }

        widgets = {
            'nimi': forms.TextInput(attrs={'placeholder': 'Nimi...', 'class': 'av-nimi'}),
            'sposti': forms.EmailInput(attrs={'placeholder': 'Sähköposti...', 'class': 'av-sposti', 'type':'email'}),
            'puh': forms.TextInput(attrs={'placeholder': 'Puhelinnumero...', 'class': 'av-puh', 'type':'tel'}),
            'osoite': forms.TextInput(attrs={'placeholder': 'Osoite...', 'class': 'av-osoite'}),
            'rekisterinumero': forms.TextInput(attrs={'placeholder': 'Rekisterinumero...', 'class': 'av-rekisterinumero'}),
            'vuosimalli': forms.NumberInput(attrs={'placeholder': 'Vuosimalli...', 'class': 'av-vuosimalli', 'type':'number', 'min':'1'}),
            'merkki': forms.TextInput(attrs={'placeholder': 'Merkki...', 'class': 'av-merkki'}),
            'malli': forms.TextInput(attrs={'placeholder': 'Malli...', 'class': 'av-malli'}),
            'kilometrit': forms.NumberInput(attrs={'placeholder': 'Kilometrit...', 'class': 'av-kilometrit', 'type':'number', 'min':'1'}),
            'lisatiedot': forms.Textarea(attrs={'placeholder': 'Lisätiedot...', 'class': 'av-lisatiedot'}),
            'pvm': forms.DateInput(attrs={'placeholder': 'Päivämäärä...', 'class': 'av-pvm', 'type':'date'}),
            'klo': forms.TimeInput(attrs={'placeholder': 'Kellonaika...', 'class': 'av-klo', 'type':'time'}),
        }
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
            'nimi': forms.TextInput(attrs={'class': 'av-nimi av-form-elem'}),
            'palaute': forms.Textarea(attrs={'class': 'av-lisatiedot av-form-elem'}),
            'sposti': forms.EmailInput(attrs={'class': 'av-sposti av-form-elem'})
        }

class PalveluValinta(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        valinta = super().create_option(name, value, label, selected, index, subindex, attrs)

        return valinta

class ajanvaraus(forms.ModelForm):
    class Meta:
        model = ajanvaraus
        fields = ('nimi', 'sposti', 'puh', 'osoite', 'rekisterinumero', 'vuosimalli', 'merkki', 'malli', 'kilometrit', 'lisatiedot', 'pvm', 'klo', 'valinta_palvelut',)
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
            'nimi': forms.TextInput(attrs={'class': 'av-nimi av-form-elem'}),
            'sposti': forms.EmailInput(attrs={'class': 'av-sposti av-form-elem', 'type':'email'}),
            'puh': forms.TextInput(attrs={'class': 'av-puh av-form-elem', 'type':'tel'}),
            'osoite': forms.TextInput(attrs={'class': 'av-osoite av-form-elem'}),
            'rekisterinumero': forms.TextInput(attrs={'class': 'av-rekisterinumero av-form-elem'}),
            'vuosimalli': forms.NumberInput(attrs={'class': 'av-vuosimalli av-form-elem', 'type':'number', 'min':'1'}),
            'merkki': forms.TextInput(attrs={'class': 'av-merkki av-form-elem'}),
            'malli': forms.TextInput(attrs={'class': 'av-malli av-form-elem'}),
            'kilometrit': forms.NumberInput(attrs={'class': 'av-kilometrit av-form-elem', 'type':'number', 'min':'1'}),
            'lisatiedot': forms.Textarea(attrs={'class': 'av-form-elem av-lisatiedot'}),
            'pvm': forms.DateInput(attrs={'class': 'av-pvm av-form-elem', 'type':'date'}),
            'klo': forms.TimeInput(attrs={'class': 'av-klo av-form-elem', 'type':'time', "min":"10:00", "max":"17:00"}),
            'valinta_palvelut': PalveluValinta
        }
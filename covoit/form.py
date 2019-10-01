from django import forms
from .models import Voiture


class CreateCovoitForm(forms.ModelForm):

    class Meta:
        model = Voiture
        labels = {
            "départ": "adresse de départ",
            "placedispo": "Place disponible",
            "heure": "Heure de départ",
        }
        fields = ["départ", "placedispo", "heure", "minute"]


class PlaceForm(forms.Form):

    addresse = forms.CharField(label="Lieu de rdv")
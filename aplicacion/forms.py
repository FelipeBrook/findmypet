from django import forms
from .models import Contacto,pet


class CoctactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields="__all__"


class petForm(forms.ModelForm):
    class Meta:
        model= pet
        fields="__all__"
from django.forms import ModelForm
from main.models import Inmueble
from django import forms

class InmuebleForm(ModelForm):
    class Meta:
        model = Inmueble
        exclude = []
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            ##completar el resto de los campos
        }
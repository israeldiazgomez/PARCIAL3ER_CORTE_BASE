from django.forms import fields
from django import forms
from apps.laboratorios.models import Laboratorio
from django.forms import fields

class LaboratorioForm(forms.ModelForm):
    class Meta: 
        model = Laboratorio
        
        fields = [
            'nombre',
            'pais'
        ]
        labels = {
            'nombre': 'Ingrese su nombre',
            'pais': 'Ingrese su pais'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
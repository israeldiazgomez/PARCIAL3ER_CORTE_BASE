from django.forms import fields
from django import forms
from apps.medicamentos.models import Medicamento
from django.forms import fields



class MedicamentoForm(forms.ModelForm):
    class Meta: 
        model = Medicamento
        
        fields = [
            'nombre',
            'laboratorio'
        ]
        labels = {
            'nombre': 'Ingrese su nombre',
            'laboratorio': 'Seleccione Laboratorio'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'laboratorio': forms.Select(attrs={'class': 'form-control'}),
            
        }
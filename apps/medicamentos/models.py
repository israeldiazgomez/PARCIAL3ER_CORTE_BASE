from django.db import models

from apps.laboratorios.models import Laboratorio

class Medicamento (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
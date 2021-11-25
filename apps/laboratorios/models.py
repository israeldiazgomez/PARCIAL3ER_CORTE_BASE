from django.db import models

class Laboratorio (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    pais = models.CharField(max_length=100, verbose_name="Nombre")
    
    
    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"
        
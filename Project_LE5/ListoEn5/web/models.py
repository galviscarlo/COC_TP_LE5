from django.db import models

# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    ingredientes = models.CharField(max_length=300, verbose_name='Ingredientes')
    preparacion = models.CharField(max_length=500, verbose_name='Preparacion')
    origen = models.CharField(max_length=100, verbose_name='Origen', null=True)


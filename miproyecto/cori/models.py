from django.db import models

# Create your models here.

class tipo_negocio(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre


class negocio(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    tipo_negocio = models.ForeignKey(tipo_negocio, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre
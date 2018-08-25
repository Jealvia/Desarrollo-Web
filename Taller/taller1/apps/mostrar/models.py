from django.db import models

# Create your models here.

class Servicios(models.Model):
    nombre=models.CharField(max_length=50)
    fechaInicio=models.DateTimeField()
    objects=models.Manager()
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    idUsuario=models.ManyToManyField(Servicios)
    user = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    objects=models.Manager()
    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre=models.CharField(max_length=255,blank=False)
    fecha=models.DateField()
    direccion=models.TextField(max_length=255)
    def __str__(self):
        return '%s' % self.nombre

class Usuario(models.Model):
    nombre_completo=models.CharField(max_length=255,blank=False)
    ciudad=models.CharField(max_length=255,blank=False)
    id_servicio=models.ManyToManyField(Servicio)
    #id_factura=models.ManyToManyField(Factura)
    def __str__(self):
        return '%s' % self.nombre_completo
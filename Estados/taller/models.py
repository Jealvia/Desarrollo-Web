from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario=models.CharField(max_length=255,blank=False)
    contasena=models.CharField(max_length=255,blank=True)
    def __str__(self):
        return '%s' % self.usuario


from djongo import models
import csv
import datetime

class Servicio(models.Model):
    nombre=models.CharField(max_length=255,blank=False)
    fecha=models.DateField()
    objects = models.DjongoManager()
    def __str__(self):
        return '%s' % self.nombre

class Factura(models.Model):
    total_factura=models.IntegerField()
    fecha=models.DateField()
    id_servicio=models.ForeignKey(Servicio,models.SET_NULL,blank=True,null=True,)
    objects = models.DjongoManager()
    def __str__(self):
        return '%s' % self.total_factura

class Usuario(models.Model):
    nombre_completo=models.CharField(max_length=255,blank=False)
    ciudad=models.CharField(max_length=255,blank=False)
    id_servicio=models.ForeignKey(Servicio,models.SET_NULL,blank=True,null=True,)
    id_factura=models.ForeignKey(Factura,models.SET_NULL,blank=True,null=True,)
    objects = models.DjongoManager()
    def __str__(self):
        return '%s' % self.nombre_completo
        
"""
with open('static/data/todosmisservicios.csv', newline='') as File:  
    reader = csv.reader(File)
    dic=[]
    for row in reader:
        serv=Servicio(nombre=row[1])
        try:
            serv.save()
        except:
            i=0
            #print("Error")
        factura=Factura(total_factura=int(row[4]),fecha=datetime.datetime.strptime(row[3],'%Y-%m-%d').date(),id_servicio=serv)
        try:
            factura.save()
        except:
            i=0
            #print("Error")
        usuario=Usuario(nombre_completo=row[0],ciudad=row[2],id_servicio=serv,id_factura=factura)
        try:
            usuario.save()
        except:
            i=0
            #print("Error")
"""
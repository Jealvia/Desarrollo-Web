from django.shortcuts import render
from app1.models import Usuario,Factura,Servicio
from datetime import date
# Create your views here


def index(request):
    return render(request,'usuarios.html')

def mostar_usuarios(request):
    if request.method=='GET':
        usuarios=Usuario.objects.all()
        contexto={'usuario': usuarios}
        return render(request,'usuarios.html',contexto)
    if request.method=='POST': 
        servicio=Servicio.objects.all().filter(nombre=request.POST['servicio'].upper())
        arr=[]
        for serv in servicio:
            arr.append(serv.id)
        user=Usuario.objects.all()
        usuarios=[]
        for usuario in user:
            if usuario.id_servicio.id in arr:
                if str(usuario.id_factura.fecha.month)==request.POST['mes']:
                    usuarios.append(usuario)
        return render(request,'usuarios.html',{'usuario':usuarios})


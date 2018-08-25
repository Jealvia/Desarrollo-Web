from django.shortcuts import render
from django.http import HttpResponse
from apps.mostrar.models import Usuarios 
# Create your views here.

def index(request):
    return render(request,'usuarios.html')


def mostar_usuarios(request):
    usuarios=Usuarios.objects.all()
    contexto={'usuario':usuarios}
    return render(request,'usuarios.html',contexto)
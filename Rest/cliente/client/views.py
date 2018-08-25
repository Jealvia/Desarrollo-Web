from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
import requests
 
def mostrarUsuario(request,pk):
    if request.method == 'GET':
        guser = requests.get('http://127.0.0.1:8000/usuario/'+str(pk)+'/')
        user = guser.json()
        lista_servicios=[]
        #print(user)
        for i in user['id_servicio']:
            servicio=requests.get('http://127.0.0.1:8000/servicio/'+str(i)+'/')
            lista_servicios.append(servicio.json())
        #print(lista_servicios)
        context = {
            'usuarios' : user,
            'servicios': lista_servicios ,
        }
        return render(request,'usuarios.html',context)

def modificarUsuario(request,user,serv):
    if request.method == 'GET':
        guser = requests.get('http://127.0.0.1:8000/usuario/'+str(user)+'/')
        user = guser.json()
        servicio=requests.get('http://127.0.0.1:8000/servicio/'+str(serv)+'/')
        lista_servicios=servicio.json()
        context = {
            'usuario' : user,
            'servicio': lista_servicios ,
        }
        return render(request,'edit-delete.html',context)

    if request.method == 'POST':
        requests.post('http://127.0.0.1:8000/usuario/modificar/'+str(serv)+'/', data= {'direccion' : request.POST['direccion']})
        print(request.POST['direccion'])
        return redirect('http://127.0.0.1:7000/usuario/'+str(user)+'/')

def eliminarServicio(request,user,serv):
    if request.method == 'POST':
        requests.post('http://127.0.0.1:8000/usuario/eliminar/'+str(serv)+'/')
        return redirect('http://127.0.0.1:7000/usuario/'+str(user)+'/')

def crearServicio(request,user):
    if request.method == 'GET':
        guser = requests.get('http://127.0.0.1:8000/usuario/'+str(user)+'/')
        user = guser.json()
        print(user)
        gserv = requests.get('http://127.0.0.1:8000/servicio/')
        print(gserv.json())
        servicios = []
        for i in gserv.json():
            servicios.append(i)
        context = {
            'usuario' : user,
            'servicios' : servicios
        }
        print(context)
        return render(request,'crear.html',context)

    if request.method == "POST":
        requests.post('http://127.0.0.1:8000/usuario/crear/'+str(user)+'/', 
        data = {'nombre' : request.POST['name'],'fecha' : request.POST["fecha_registro"],
        'direccion' : request.POST['direccion']})
        return redirect('http://127.0.0.1:7000/usuario/'+str(user)+'/')
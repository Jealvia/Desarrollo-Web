from django.shortcuts import render,redirect
from appRest.models import Servicio,Usuario
from appRest.serializers import ServicioSerializer,UsuarioSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from django.http import Http404,JsonResponse,HttpResponse
from appRest.forms import ServicioForm
from django.views.decorators.csrf import csrf_exempt

class UsuarioListar(APIView):
    @csrf_exempt
    def get(self, request,pk):
        users = get_object_or_404(Usuario, id=pk)
        serializer = UsuarioSerializer(users)
        return JsonResponse(serializer.data, safe = False)

class ServicioListarTodos(APIView):
    @csrf_exempt
    def get(self, request):
        servicio = Servicio.objects.all()
        serializer = ServicioSerializer(servicio,many=True)
        return JsonResponse(serializer.data, safe = False)

class ServicioListar(APIView):
    @csrf_exempt
    def get(self, request,serv):
        servicio = get_object_or_404(Servicio, pk=serv)
        serializer = ServicioSerializer(servicio)
        return JsonResponse(serializer.data, safe = False)
        
#Mostrar servicio y modificar
class ServicioCrear(APIView):
    def get(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        serializer = ServicioSerializer(servicio)
        return Response({'serializer': serializer, 'servicio': servicio})
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.direccion=request.POST['direccion']
        servicio.save()
        serializer = ServicioSerializer(servicio)
        if not serializer.is_valid():
            return HttpResponse(status=404)
        serializer.save()
        return JsonResponse(serializer.data)
#Eliminar
class ServicioEliminar(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'eliminar.html'
    def get(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        serializer = ServicioSerializer(servicio)
        return Response({'serializer': serializer, 'servicio': servicio})
    def post(self, request, pk):
        servicio = get_object_or_404(Servicio, pk=pk)
        servicio.delete()
        return HttpResponse(status=204)
        
#Crear
class ServicioDetails(APIView):
    def post(self, request, pk):
        user=get_object_or_404(Usuario, id=pk)
        datos={'nombre':request.POST['nombre'],'fecha':request.POST['fecha'],'direccion':request.POST['direccion']  }
        serializer = ServicioSerializer(data=datos)
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            serv = Servicio.objects.all().last()
            print(serv)
            user.id_servicio.add(serv)    
            user.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ServicioList(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class ServicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer



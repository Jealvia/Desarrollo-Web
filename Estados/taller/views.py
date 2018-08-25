from django.shortcuts import render,redirect
from taller.models import Usuarios
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.


def logear(request):
    if request.method=='GET':
        context={}
        return render(request,'login.html',context)
    
def prueba(request):
    if request.method=='GET':
        print(request.session["nombre"])
        if 'contra' in request.COOKIES:
            print("Hola")
            context={'prueba': request.session["nombre"],
                     'contraena': request.COOKIES['contra']  }
            return render(request,'page2.html',context)
    if request.method=='POST':
        try:
            user=Usuarios.objects.get(usuario=request.POST['nombre'])
        except:
            context={'error':'Error usuario incorrecto'}
            return render(request,'login.html',context)
        if(user.contasena==request.POST['contrasena']):
            #print("Hola")
            request.session["nombre"]=request.POST['nombre']

            response = render(request, 'page2.html')
   
            response.set_cookie('contra', 'Usuario logeado correctamente')
            return redirect('http://127.0.0.1:8000/page2/')
            #return response
            #return render(request,'page2.html',contexto)


def final(request):
    if request.method=='GET':
        context={'prueba': request.session["nombre"],
                     'contraena': request.COOKIES['contra']  }
        return render(request,'page3.html',context)
    
    if request.method=='POST':
        if 'contra' in request.COOKIES:
            #contexto={'nombre':request.POST['nombre'],'contra':request.COOKIES['contra']}
            return redirect('http://127.0.0.1:8000/page3/')
            #return render(request,'page3.html',contexto)
        


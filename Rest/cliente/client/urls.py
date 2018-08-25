from django.conf.urls import url, include
from client import views

urlpatterns = [
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.mostrarUsuario,name='listar_usuarios'),
    url(r'^usuario/editar/(?P<user>[0-9]+)/(?P<serv>[0-9]+)/$', views.modificarUsuario,name='editar_usuarios'),
    url(r'^usuario/eliminar/(?P<user>[0-9]+)/(?P<serv>[0-9]+)/$', views.eliminarServicio,name='eliminar_servicio'),
    url(r'^usuario/servicio/crear/(?P<user>[0-9]+)/$', views.crearServicio,name='crear_servicio'),
]

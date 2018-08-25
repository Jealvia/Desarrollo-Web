from django.conf.urls import url, include
from appRest import views

urlpatterns = [
    url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuarioListar.as_view(),name='listar_usuarios'),
    url(r'^servicio/$', views.ServicioListarTodos.as_view(),name='todos_servicio'),
    url(r'^servicio/(?P<serv>[0-9]+)/$', views.ServicioListar.as_view(),name='listar_servicio'),
    url(r'^usuario/modificar/(?P<pk>[0-9]+)/$', views.ServicioCrear.as_view(),name='crear_servicio'),
    url(r'^usuario/eliminar/(?P<pk>[0-9]+)/$', views.ServicioEliminar.as_view(),name='eliminar_servicio'),
    url(r'^usuario/crear/(?P<pk>[0-9]+)/$', views.ServicioDetails.as_view(),name='nuevo_servicio'),
    url(r'^usuarios/(?P<pk>[-\w]+)/$', views.UsuarioDetail.as_view()),
    url(r'^servicio/$', views.ServicioList.as_view()),
    
    ]
#urlpatterns = format_suffix_patterns(urlpatterns)
"""
    url(r'^usuarios/(?P<pk>[-\w]+)/$', views.UsuarioDetail.as_view()),
    url(r'^servicio/$', views.ServicioList.as_view()),
    url(r'^servicio/(?P<pk>[0-9]+)/$', views.ServicioDetail.as_view()),
    url(r'^factura/$', views.FacturaList.as_view()),
    url(r'^factura/(?P<pk>[0-9]+)/$', views.FacturaDetail.as_view()),
"""



from django.conf.urls import url, include
from taller import views

urlpatterns = [
    url(r'^login/$',views.logear,name='logearse'),
    url(r'^page2/$',views.prueba,name='prueba'),
    url(r'^page3/$',views.final,name='final'),
]

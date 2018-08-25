from django.conf.urls import url,include

from apps.mostrar.views import mostar_usuarios

urlpatterns = [
    url(r'^$', mostar_usuarios),
]

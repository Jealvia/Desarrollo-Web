from rest_framework import serializers
from appRest.models import Servicio,Usuario

"""
class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('total_factura', 'fecha', 'id_servicio')
"""

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('id', 'nombre', 'fecha','direccion')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre_completo', 'ciudad', 'id_servicio')
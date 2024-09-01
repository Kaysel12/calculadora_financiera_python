from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CalculoInversionSerializer(serializers.Serializer):
    producto = serializers.IntegerField()
    en_reinversion = serializers.BooleanField()
    plazo = serializers.IntegerField()
    fecha_creacion = serializers.DateTimeField()
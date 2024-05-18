from rest_framework import serializers
from .models import Producto, Precio

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    precios = PrecioSerializer(many=True, read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'

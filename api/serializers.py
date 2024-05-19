from rest_framework import serializers
from .models import Producto, Precio, Compra

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precio
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    precios = PrecioSerializer(many=True, read_only=True)
    
    class Meta:
        model = Producto
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_descripcion = serializers.CharField(source='producto.descripcion', read_only=True)
    producto_precio_actual = serializers.DecimalField(source='producto.precio_actual', max_digits=10, decimal_places=2, read_only=True)
    #Compra.objects.all().delete()
    class Meta:
        model = Compra
        fields = ['id', 'producto', 'producto_nombre', 'producto_descripcion', 'producto_precio_actual', 'cantidad', 'fecha']


from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer

class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.filter(activo=True)
    serializer_class = ProductoSerializer

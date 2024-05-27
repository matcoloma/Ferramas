from rest_framework import generics, status
from rest_framework.response import Response
from .models import Categoria, Producto, Carrito, ItemCarrito
from .serializers import CategoriaSerializer, ProductoSerializer, CarritoSerializer, ItemCarritoSerializer

class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CarritoDetail(generics.RetrieveUpdateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        carrito_id = kwargs.get('pk')  # Obtener el ID del carrito desde los argumentos de la vista
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad', 1)

        try:
            carrito = Carrito.objects.get(id=carrito_id)  # Usar el ID del carrito para obtener el carrito
        except Carrito.DoesNotExist:
            return Response({"detail": "Carrito not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            return Response({"detail": "Producto not found."}, status=status.HTTP_404_NOT_FOUND)

        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        if not created:
            item.cantidad += int(cantidad)
        else:
            item.cantidad = int(cantidad)
        item.save()

        return Response(ItemCarritoSerializer(item).data, status=status.HTTP_201_CREATED)

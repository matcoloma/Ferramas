from django.urls import path
from .views import CategoriaListCreate, ProductoListCreate, CarritoDetail

urlpatterns = [
    path('categorias/', CategoriaListCreate.as_view(), name='categoria-list-create'),
    path('productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('carrito/<int:pk>/', CarritoDetail.as_view(), name='carrito-detail'),
]
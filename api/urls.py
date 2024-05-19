from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CompraViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'compras', CompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

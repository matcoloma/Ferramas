# tienda/productos/management/commands/seed.py
import json
from django.core.management.base import BaseCommand
from api.models import Categoria, Producto

class Command(BaseCommand):
    help = 'Carga datos desde un archivo JSON'

    def handle(self, *args, **kwargs):
        with open('seed.json') as file:
            data = json.load(file)
            for item in data:
                categoria_data = item['campos']
                productos_data = categoria_data.pop('productos')
                categoria, created = Categoria.objects.get_or_create(nombre=categoria_data['nombre'])
                for producto_data in productos_data:
                    Producto.objects.get_or_create(categoria=categoria, **producto_data)
        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))
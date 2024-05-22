import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferremas_api.settings')
django.setup()

from productos.models import Categoria, Producto

def populate():
    materiales_basicos = [
        {'nombre': 'Cemento', 'descripcion': 'Descripción de Cemento', 'precio': 1000.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-CEM', 'stock': 50},
        {'nombre': 'Arena', 'descripcion': 'Descripción de Arena', 'precio': 500.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-ARE', 'stock': 50},
        {'nombre': 'Ladrillos', 'descripcion': 'Descripción de Ladrillos', 'precio': 300.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-LAD', 'stock': 50},
        {'nombre': 'Acabados', 'descripcion': 'Descripción de Acabados', 'precio': 2000.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-ACA', 'stock': 50},
        {'nombre': 'Pinturas', 'descripcion': 'Descripción de Pinturas', 'precio': 1500.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-PIN', 'stock': 50},
        {'nombre': 'Barnices', 'descripcion': 'Descripción de Barnices', 'precio': 1200.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-BAR', 'stock': 50},
        {'nombre': 'Cerámicos', 'descripcion': 'Descripción de Cerámicos', 'precio': 1800.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-CER', 'stock': 50},
    ]

    equipos_seguridad = [
        {'nombre': 'Casos', 'descripcion': 'Descripción de Casos', 'precio': 800.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-CAS', 'stock': 50},
        {'nombre': 'Guantes', 'descripcion': 'Descripción de Guantes', 'precio': 300.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-GUA', 'stock': 50},
        {'nombre': 'Lentes de Seguridad', 'descripcion': 'Descripción de Lentes de Seguridad', 'precio': 600.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-LEN', 'stock': 50},
        {'nombre': 'Accesorios Varios', 'descripcion': 'Descripción de Accesorios Varios', 'precio': 200.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-ACC', 'stock': 50},
    ]

    herramientas_manuales = [
        {'nombre': 'Martillos', 'descripcion': 'Descripción de Martillos', 'precio': 900.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-MAR', 'stock': 50},
        {'nombre': 'Destornilladores', 'descripcion': 'Descripción de Destornilladores', 'precio': 400.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-DES', 'stock': 50},
        {'nombre': 'Llaves', 'descripcion': 'Descripción de Llaves', 'precio': 700.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-LLA', 'stock': 50},
        {'nombre': 'Taladros', 'descripcion': 'Descripción de Taladros', 'precio': 3500.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-TAL', 'stock': 50},
        {'nombre': 'Sierras', 'descripcion': 'Descripción de Sierras', 'precio': 2200.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-SIE', 'stock': 50},
        {'nombre': 'Lijadoras', 'descripcion': 'Descripción de Lijadoras', 'precio': 1800.00, 'modelo': 'Modelo XYZ', 'marca': 'Marca ABC', 'codigo': 'COD-LIJ', 'stock': 50},
    ]

    categoria_materiales = Categoria.objects.get_or_create(nombre='Materiales Básicos')[0]
    categoria_materiales.save()

    categoria_equipos = Categoria.objects.get_or_create(nombre='Equipos de Seguridad')[0]
    categoria_equipos.save()

    categoria_herramientas = Categoria.objects.get_or_create(nombre='Herramientas Manuales')[0]
    categoria_herramientas.save()

    for prod in materiales_basicos:
        producto = Producto.objects.get_or_create(
            nombre=prod['nombre'],
            descripcion=prod['descripcion'],
            precio=prod['precio'],
            modelo=prod['modelo'],
            marca=prod['marca'],
            codigo=prod['codigo'],
            stock=prod['stock'],
            categoria=categoria_materiales,
            activo=True
        )[0]
        producto.save()

    for prod in equipos_seguridad:
        producto = Producto.objects.get_or_create(
            nombre=prod['nombre'],
            descripcion=prod['descripcion'],
            precio=prod['precio'],
            modelo=prod['modelo'],
            marca=prod['marca'],
            codigo=prod['codigo'],
            stock=prod['stock'],
            categoria=categoria_equipos,
            activo=True
        )[0]
        producto.save()

    for prod in herramientas_manuales:
        producto = Producto.objects.get_or_create(
            nombre=prod['nombre'],
            descripcion=prod['descripcion'],
            precio=prod['precio'],
            modelo=prod['modelo'],
            marca=prod['marca'],
            codigo=prod['codigo'],
            stock=prod['stock'],
            categoria=categoria_herramientas,
            activo=True
        )[0]
        producto.save()

if __name__ == '__main__':
    print("Populando la base de datos...")
    populate()
    print("Población completada.")

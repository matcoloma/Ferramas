# Proyecto FERREMAS

Este proyecto consiste en la construcción de una API para consultar información detallada de productos, permitir pedidos y mantener inventarios actualizados para las sucursales de FERREMAS. El proyecto está desarrollado con Django y Django REST Framework.

## Requisitos Previos

- Python 3.12.3+
- Pip (Python package manager)
- Virtualenv (recomendado)

## Instalación y Configuración


1. **Clonar el repositorio** 
   ```bash
   git clone https://github.com/matcoloma/Ferramas.git
   cd ferremas
2. **Creación del entorno virtual y activación** 
    ```bash
    pip3 install virtualenv
    virtualenv venv
    # El siguiente comando es solo para windows
    call venv\Scripts\activate.bat
    # En macOS y Linux
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate

3. **Instalar las dependencias** 
    ```bash
    pip install -r requirements.txt

4. **Aplicar migraciones** 
    ```bash
    python manage.py makemigrations
    python manage.py migrate
5. **Ejecutar** 
    ```bash
    python manage.py loaddata seed
6. **Ejecuta el servidor de desarrollo** 
    ```bash
    python manage.py runserver
7. **USO** 
    ```bash
    Una vez que el servidor esté en funcionamiento, podrás acceder a la API en http://127.0.0.1:8000/api/


Este archivo `README.md` proporciona instrucciones claras y concisas para clonar el repositorio, configurar el entorno de desarrollo, instalar las dependencias necesarias, aplicar las migraciones de la base de datos y ejecutar el servidor de desarrollo de Django. Además, ofrece orientación sobre el uso de la API.


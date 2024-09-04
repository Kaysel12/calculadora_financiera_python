# Bienvenido al Proyecto de Calculadora Financiera

<p align="center">
    <img alt="Django Logo" title="Django Logo" src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" width="450">
</p>

## Leer Primero

Lo siguiente se descubrió al construir este proyecto:

- La base de datos se encuentra en MySQL y se utiliza en combinación con Django para manejar las operaciones de inversión y productos.

## Comenzando

¡Bienvenido al Proyecto de Calculadora Financiera! Este proyecto está construido con Django y MySQL, y está configurado para ejecutarse con Docker. A continuación, se presentan algunos recursos para ayudarte a comenzar:

### Documentación de Referencia

Para más información, por favor consulta las siguientes secciones:

- [Documentación Oficial de Django](https://docs.djangoproject.com/en/5.1/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)

### Guías

Las siguientes guías ilustran cómo utilizar algunas características concretas:

- [Construyendo un Servicio Web RESTful con Django](https://www.django-rest-framework.org/tutorial/quickstart/)
- [Configuración de MySQL con Django](https://docs.djangoproject.com/en/5.1/ref/databases/#mysql)
- [Documentación de DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/usage.html)

### Swagger

Este proyecto incluye [DRF Spectacular](https://drf-spectacular.readthedocs.io/en/latest/), una herramienta para la documentación de APIs. Puedes visualizar la documentación interactiva de tu API accediendo a:

- `http://localhost:8000/swagger/` (si estás ejecutando el proyecto localmente)

### Endpoints Disponibles

#### Producto

- **`GET /productos/`**
  - **Descripción**: Obtiene una lista de todos los productos.
  - **Permiso**: Autenticado.

#### Calculo de Inversión

- **`POST /calcular-inversion/`**
  - **Descripción**: Calcula las fechas de inversión basadas en los datos proporcionados.
  - **Parámetros en el cuerpo de la solicitud**:
    - `producto`: ID del producto.
    - `en_reinversion`: Booleano que indica si está en reinversión.
    - `plazo`: Plazo de inversión en días.
    - `fecha_creacion`: Fecha de creación en formato `YYYY-MM-DD HH:MM:SS`.
  - **Respuesta**:
    - `producto`: ID del producto.
    - `plazo`: Plazo de inversión en días.
    - `fecha_inicio`: Fecha calculada de inicio.
    - `fecha_fin`: Fecha calculada de fin.
    - `plazo_real`: Plazo real en días.

### Importación de la Base de Datos

Para trabajar con la base de datos MySQL, debes importar los archivos de base de datos que se encuentran en la carpeta `inversiones_database`. Sigue estos pasos:

1. **Abrir MySQL Workbench**.
2. **Conectar a tu servidor MySQL**. Asegúrate de que el contenedor MySQL esté corriendo si lo estás utilizando.
3. **Importar los archivos SQL**. Ve a `Server > Data Import` y selecciona `Import from Dump Project Folder`. Deberán tener un archivo llamado dumps, este es un ejemplo: `/Users/kayselnunez/dumps` para pasar el archivo `inversiones_database` en ese espacio y poder hacer las importaciones. Elige los archivos `.sql` que se encuentran en `inversiones_database` y cárgalos en la base de datos `inversiones`.

### Acceso al Panel de Administración

El superusuario para acceder al panel de administración de Django se puede crear con las siguientes credenciales predeterminadas:

- **Username**: `admin`
- **Password**: `admin`

Para acceder al panel de administración, visita:


### Ejecutar el Proyecto con Docker

Asegúrate de que Docker esté instalado y en funcionamiento en tu máquina. Luego, ejecuta el siguiente comando para construir e iniciar los contenedores:

```bash docker-compose up --build```

- http://localhost:8000/swagger/

- También, para crear el superusuario debes entrar a la terminal del proyecto una vez este corriendo en el docker y escribir lo siguiente:

```docker-compose exec calculadora python manage.py createsuperuser```
Ahí escribir el super usuario **username: admin** y **password: admin**

- Luego de esto, se agregaran datos de los productos con los siguientes comandos en la terminal:

```docker-compose exec calculadora python manage.py shell```
Cuando habra el shell, copiar y pegar lo siguiente

from calculadora.models import Producto  # Reemplaza `Producto` con el nombre de tu modelo

- productos = [
    {'nombre': 'Plazo Fijo a 30 días', 'dias_operativos_in': 2, 'dias_operativos_out': 1, 'dias_reinversion_in': 1, 'dias_reinversion_out': 1, 'hora_operativa': '09:00:00'},
    {'nombre': 'Certificado de Depósito 90 días', 'dias_operativos_in': 3, 'dias_operativos_out': 2, 'dias_reinversion_in': 2, 'dias_reinversion_out': 2, 'hora_operativa': '10:00:00'},
    {'nombre': 'Fondo Mutuo Conservador', 'dias_operativos_in': 1, 'dias_operativos_out': 1, 'dias_reinversion_in': 1, 'dias_reinversion_out': 1, 'hora_operativa': '14:00:00'},
    {'nombre': 'Letras del Tesoro a 180 días', 'dias_operativos_in': 3, 'dias_operativos_out': 3, 'dias_reinversion_in': 0, 'dias_reinversion_out': 0, 'hora_operativa': '11:00:00'},
    {'nombre': 'Bono Corporativo a 1 año', 'dias_operativos_in': 5, 'dias_operativos_out': 5, 'dias_reinversion_in': 0, 'dias_reinversion_out': 0, 'hora_operativa': '12:00:00'},
    {'nombre': 'Depósito a Plazo a 60 días', 'dias_operativos_in': 2, 'dias_operativos_out': 1, 'dias_reinversion_in': 1, 'dias_reinversion_out': 1, 'hora_operativa': '09:30:00'},
    {'nombre': 'Fondo de Inversión Agresivo', 'dias_operativos_in': 1, 'dias_operativos_out': 2, 'dias_reinversion_in': 2, 'dias_reinversion_out': 2, 'hora_operativa': '15:00:00'},
    {'nombre': 'Acciones Preferentes', 'dias_operativos_in': 3, 'dias_operativos_out': 3, 'dias_reinversion_in': 0, 'dias_reinversion_out': 0, 'hora_operativa': '13:00:00'},
    {'nombre': 'Pagaré Bancario a 90 días', 'dias_operativos_in': 2, 'dias_operativos_out': 2, 'dias_reinversion_in': 1, 'dias_reinversion_out': 1, 'hora_operativa': '10:30:00'},
    {'nombre': 'Obligación Subordinada a 2 años', 'dias_operativos_in': 4, 'dias_operativos_out': 4, 'dias_reinversion_in': 0, 'dias_reinversion_out': 0, 'hora_operativa': '11:30:00'}
]

for data in productos:
    Producto.objects.create(**data)


*Y luego dar enter. con eso tenemos para que el proyecto funcione.



Este archivo `README.md` debería proporcionar una guía clara para configurar y ejecutar tu proyecto, así como para acceder a la base de datos y la interfaz de administración.

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
3. **Crear una nueva base de datos** llamada `inversiones` si no existe aún.
4. **Importar los archivos SQL**. Ve a `Server > Data Import` y selecciona `Import from Self-Contained File`. Elige los archivos `.sql` que se encuentran en `inversiones_database` y cárgalos en la base de datos `inversiones`.

### Acceso al Panel de Administración

El superusuario para acceder al panel de administración de Django se puede crear con las siguientes credenciales predeterminadas:

- **Username**: `admin`
- **Password**: `admin`

Para acceder al panel de administración, visita:


### Ejecutar el Proyecto con Docker

Asegúrate de que Docker esté instalado y en funcionamiento en tu máquina. Luego, ejecuta el siguiente comando para construir e iniciar los contenedores:

```bash
docker-compose up --build ```

- http://localhost:8000/swagger/






- Este archivo `README.md` debería proporcionar una guía clara para configurar y ejecutar tu proyecto, así como para acceder a la base de datos y la interfaz de administración.

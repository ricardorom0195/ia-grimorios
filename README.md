# Asignación de grimorios

En el Reino del Trébol, el Rey Mago necesita un sistema para la academia de magia que administre el registro de solicitud de estudiantes y la asignación aleatoria de sus Grimorios. Los Grimorios se clasifican según el tipo de trébol en la portada, y los estudiantes según sus afinidades mágicas específicas.

Se realizaron varias apis rest para el registro, actualización y borrado de estudiantes así como la asignación de grimorios entre algunas otras opciones.

### Pre-requisitos 📋

Para la correcta instalación y funcionamiento de este proyecto se requiere se tengan previamente instalados las siguientes tecnologias

<ol>
  <li>Python 3.9</li>
  <li>Framework fastapi</li>
  <li>Docker</li>
  <li>Docker-Compose</li>
</ol>

## Comenzando 🚀

Primeramente hacer un clone de este repositorio de la rama master.

### Instalación 🔧

Para comenzar se va a levantar la base de datos postgresql la cual se tiene en un contenedor docker, para esto se utilizara docker-compose.

Desde la terminal debe ingresar a la siguiente ruta init/database, en la cual se encuentra lo necesario para levantar nuestra base de datos. Contamos también con un archivo .env el cual tiene las credenciales de la base de datos para cargar como variable de entorno en el contenedor. En este momento pueden realizar los ajustes que se requieran a las variables de entorno o pueden quedarse como están.

<img src="https://github.com/ricardorom0195/ia-grimorios/blob/main/readme_images/docker_env.png?raw=true" alt="Variables de entorno" caption="Variables de entorno docker">

Ahora solo se debe levantar el contenedor con el siguiente comando:

```bash
docker-compose up -d
```

Con esto el contenedor se empezara a contruir y dentro de el la base de datos.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/docker_db.png?ref_type=heads">

Lo siguiente que hay que hacer es moverse a la ruta int/project y ejecutar lo siguiente:

```bash
pip install -r requirements.txt
```

Al ejecutarlo se instalaran todas las librerias python necesarias para poder ejecutar el proyecto.

A partir de este punto ya tenemos lo necesario para poder levantar nuestros servicios con fast api, para esto pasamos a la ruta grimorio/ y ejecutamos el siguiente comando:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 5001
```

Al hacerlo nuestro servicios se levantaron en nuestro localhost en el puerto 5001 y las apis estan listas para recibir peticiones.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/proyecto_arriba.png">

## Funcionamiento

Para las pruebas de los servicos se puede obtar por usar postman o la misma documentación del proyecto en la url http://127.0.0.1:5001/ nos permite hacer peticiones.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/Apis.png">

Para estas pruebas se utilizara postman y la colección para importar las apis se encuentra en la carpeta init en el archivo Magia.postman_collection.

Para este proyecto de crearon 6 apis test las cuales son:

### Registro de solicitud

Se guardan por primera vez los datos del estudiante en base de datos

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/registro.png">

### Actualización de solicitud

Permite modificar la data guardada en en el servicio de registro

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/update.png">

### Borrado de solicitud

Elimina el registro de solicitud del estudiante.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/borrado.png">

### Cambio de status de solicitud

En esta api se puede aceptar o rechazar al estudiante, en caso de aceptarlo se le asignara un grimorio.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/status.png">

### Obteneción de solicitudes

Trae todos los registros de solicitudes que se tengan en base de datos.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/get_solicitudes.png">

### Obteneción de asignaciones

Nos trae los registros de grimorios y cuantos usuarios pertenecen a cada uno.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/get_grimorios.png">

## Pruebas unitarias

Para las pruebas unitarias de este proyecto se utilizo la libreria pytest.

Para correr las pruebas debemos colocarnos en nuestra terminal en la carpeta grimorio/test y ejecutar el comando:

```bash
pytest -v
```
Al hacerlo comenzara la ejecución de las pruebas unitarias.

<img src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/unit_test.png">

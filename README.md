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

Para empezar se va a levantar primero la base de datos postgresql la cual se tiene en un contenedor docker, para esto se utilizara docker-compose.

Desde la terminal debe ingresar a la siguiente ruta init/database, en la cual se encuentra lo necesario para levantar nuestra base de datos. Contamos también con un archivo .env el cual tiene las credenciales de la base de datos para cargar como variable de entorno en el contenedor.

<image src="https://gitlab.com/prueba_ia/grimonios/-/raw/main/readme_images/docker_env.png?ref_type=heads" alt="Variables de entorno" caption="Variables de entorno docker">

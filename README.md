
# Herramienta a Ultilizar TASKFILE (https://taskfile.dev/)

# Correr el siguiente codigo en al terminal de BASH
   sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d

# Luego de la instalacion del binario seguir los siguientes pasos:

# Para montar las carpetas necesarias para el proyecto:
    en la terminal correr el comando:
        ./bin/task pre_project
    Cargar las credenciales en el archivo .env

# Para correr el programa:
    en la terminal correr el comando:
        ./bin/task start_project

# Para bajar el programa:
    en la terminal correr el comando:
        ./bin/task down_project
# Para "resetear" el programe carpetas:
    en la terminal correr el comando:
        ./bin/task cleanup
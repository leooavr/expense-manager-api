<p align="center">
  <img src="./static/img/fastapi.png"/>
</p>

#
#  Expense Manager 
## Bienvenido a mi api personal para control de gastos

En el proyecto actual se utilizaron los siguientes conocimientos:
```
Python 
FastAPI
Docker
ORM
Postgres
```
## Pasos para la ejecución del proyecto
1. Clonamos el repositorio en alguna carpeta alojada en su ordenador
2. Ingresamos a la carpeta por medio de comandos y abrimos Visual Studio u otro editor de código
3. Cambiamos el archivo **.env.template** a **.env** y actualizamos las credenciales de ser necesario
4. Abrimos Docker desktop
4. Ejecutamos en consola dentro del directorio del proyecto el siguiente comando:
```
docker-compose up -d
```
5. Esperamos que se levanten los contenedores y accedemos a localhost:8000/docs
6. Lo primero que debenos ejecutar es la funcion **create_tables** para crear las tablas en la base de datos antes de realizar cualquier inserción
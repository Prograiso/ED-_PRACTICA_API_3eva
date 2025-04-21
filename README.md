# ED-_PRACTICA_API_3eva
Trabajo sobre la API de Entornos de Desarrollo

## Prueba del commit

Para la parte de la base de datos , hemos hecho el codigo primero en mariadb porque es como lo se hacer , y luego he utilizado IA para pasar  ese codigo en SQLite.

el codigo que habiamos hecho nosotros:
CREATE TABLE coche (
    matricula VARCHAR(10) PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    color VARCHAR(30),
    precio DECIMAL(10,2),
    stock INT,
    kilometros INT
);

el que nos ha dado la IA: 
CREATE TABLE coche (
    matricula TEXT PRIMARY KEY,
    marca TEXT,
    modelo TEXT,
    color TEXT,
    precio REAL,
    stock INTEGER,
    kilometros INTEGER
);


## Creado Inicio HTMl
- Hemos usado los apuntes de Don ciro, posiblemente se deba ir modificando esta página según los endpoints.

## Creación del main.py
- Hemos creado main.py, requirements y vinculado con templates a la pagina de inicio html, para esto hemos usado [Real Python](https://realpython.com) traducida y pregunta sobrecomo vincularlo a la Ia.

## Creación de endpoints y modificación de html 

-hemos creado nuevos endpoints, buscar, borrar, añadir, (con mensajes de error), hemos adaptado el html para ello mediante formularios, utilizado render_template, se ha usado [Flask palletsprojects](https://flask.palletsprojects.com/en/latest/quickstart/#rendering-templates), además de  [digital ocean](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application), además de la IA parala correcta aplicación y dudas de uso.
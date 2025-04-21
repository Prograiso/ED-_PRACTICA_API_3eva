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




# IMPORTAR LIBRERÍAS

from flask import Flask, request, send_file
from flask_cors import CORS
from JGVutils import SQLiteConnection 




# CONFIGURAR APLICACIÓN
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

#CONFIGURAR PAGINA
@application.route("/", methods=["GET"])
def inicio():
    return send_file("inicio.html")

#conexion a la base de datos

@application.route("/conexion", methods=["GET"])
def devolver_coches():
    conexion = SQLiteConnection("BaseDeDatos.db")
    coche = conexion.execute_query("SELECT * FROM coche")
    return coche



#añadir a la base de datos

@application.route("/add-car", methods = ["POST"])
def add_coche():
    datos= request.form
    matricula = datos["matricula"]
    marca = datos["marca"]
    modelo = datos["modelo"]
    color = datos["color"]
    precio = datos["precio"]
    stock = datos["stock"]
    kilometros = datos["kilometros"]
    conexion = SQLiteConnection("BaseDeDatos.db")
    conexion.execute_query("INSERT INTO coche (matricula,marca,modelo,color,precio,stock,kilometros) VALUES (?,?,?,?,?,?,?)",[matricula,marca,modelo,color,precio,stock,kilometros])
    return "Se ha añadido correctamente"


#eliminar coche de la db
@application.route("/borrar", methods=["POST"])
def borrar_coche():
    matricula = request.form.get("matricula")
    if not matricula:
        return send_file("inicio.html", error="Debes proporcionar una matrícula")

    conexion = SQLiteConnection("baseDeDatos.db")
    query = "DELETE FROM coche WHERE matricula = ?"
    try:
        conexion.execute_query(query, (matricula,))
        mensaje = f"Coche con matrícula {matricula} eliminado correctamente"
        return send_file("inicio.html", mensaje=mensaje)
    except Exception as e:
        return send_file("inicio.html", error=str(e))

#buscar coche en la db
@application.route("/buscar", methods=["GET"])
def buscar_coches():
    parametro = request.form.get("parametro")
    valor = request.form.get("valor")
    if not parametro or not valor:
        return send_file("inicio.html", error="Faltan parámetros de búsqueda", coches=[])

    conexion = SQLiteConnection("baseDeDatos.db")
    query = f"SELECT * FROM coche WHERE {parametro} LIKE ?"
    try:
        coches = conexion.execute_query(query, (f"%{valor}%",))
        return send_file("{coches}", coches=coches)
    except Exception as e:
        return "error, no se"
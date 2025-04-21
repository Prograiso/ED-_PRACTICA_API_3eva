
# IMPORTAR LIBRERÍAS
from flask import Flask, request, render_template
from flask_cors import CORS
from JGVutils import SQLiteConnection


# CONFIGURAR APLICACIÓN
application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

#CONFIGURAR PAGINA
@application.route("/inicio", methods=["GET"])
def inicio():
    return render_template("inicio.html")

#conexion a la base de datos

@application.route("/conexion", methods=["GET"])
def devolver_coches():
    conexion = SQLiteConnection("baseDeDatos.db")
    coche = conexion.execute_query("SELECT * FROM coche")
    return coche

#eliminar coche de la db
@application.route("borrar", methods=["POST"])
def borrar_coche():
    matricula = request.form.get("matricula")
    if not matricula:
        return render_template("inicio.html", error="Debes proporcionar una matrícula")

    conexion = SQLiteConnection("baseDeDatos.db")
    query = "DELETE FROM coche WHERE matricula = ?"
    try:
        conexion.execute_query(query, (matricula,))
        mensaje = f"Coche con matrícula {matricula} eliminado correctamente"
        return render_template("inicio.html", mensaje=mensaje)
    except Exception as e:
        return render_template("inicio.html", error=str(e))

#buscar coche en la db
@application.route("/buscar", methods=["POST"])
def buscar_coches():
    parametro = request.form.get("parametro")
    valor = request.form.get("valor")
    if not parametro or not valor:
        return render_template("inicio.html", error="Faltan parámetros de búsqueda", coches=[])

    conexion = SQLiteConnection("baseDeDatos.db")
    query = f"SELECT * FROM coche WHERE {parametro} LIKE ?"
    try:
        coches = conexion.execute_query(query, (f"%{valor}%",))
        return render_template("inicio.html", coches=coches)
    except Exception as e:
        return render_template("inicio.html", error=str(e), coches=[])
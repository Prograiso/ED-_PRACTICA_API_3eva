
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
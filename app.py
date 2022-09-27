from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from db.repository import Repository

from routes.users_route import user_module
from routes.mesas_route import mesas_module
from routes.partido_route import partido_module
from routes.resultados_route import resultados_module

config = dotenv_values('.env')
app = Flask(__name__)
cors =CORS(app)

app.register_blueprint(user_module,url_prefix="/usuarios")
app.register_blueprint(mesas_module,url_prefix="/mesas")
app.register_blueprint(partido_module,url_prefix="/partidos")
app.register_blueprint(resultados_module,url_prefix="/resultados")


@app.route('/')

def holamundo():
    diccionario = { 
                    "mensaje":"Hola usuario:"
                  }
    return jsonify(diccionario)

if __name__ == '__main__':
    app.run(host='localhost', port=config["PORT"], debug=True)
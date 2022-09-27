from flask import jsonify,request, Blueprint
from controllers.resultados_controller import ResultadosController


resultados_module = Blueprint('resultados', __name__)
controller = ResultadosController()

@resultados_module.get('/')
#@logger
def get_resultados(): 
    return jsonify(controller.get())

@resultados_module.get('/<string:id>')
def showresultados(id): 
    return jsonify(controller.get_by_id(id))

@resultados_module.post('/mesas/<string:mesas_id>/usuarios/<string:usuarios_id>')
#@logger
def create_resultados(mesas_id, usuarios_id):
  return jsonify(controller.create(request.get_json(),mesas_id, usuarios_id)), 201
  
@resultados_module.put('/<string:id>')
def update_user(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@resultados_module.delete('/<string:id>')
def delete_resultados(id):
  controller.delete(id)
  return jsonify({}), 204

@resultados_module.get('/obtenermesasid/<string:id>')
def get_mesas_id(id):
  return jsonify(controller.get_mesas_id(id))

@resultados_module.get('/obtenermesas')
def get_all_table():
  return jsonify(controller.get_all_table())

@resultados_module.get('/obtenersumamesas')
def query_groupby():
  return jsonify(controller.query_groupby())

@resultados_module.get('/obtenervotospartido')
def get_match():
  return jsonify(controller.get_match())



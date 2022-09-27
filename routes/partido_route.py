from flask import jsonify, request, Blueprint
from controllers.partido_controller import PartidoController
#from decorators.logger_decorator import logger

partido_module= Blueprint('partidos', __name__)
controller= PartidoController()

@partido_module.get('/')
#@logger
def get_partido():
  return jsonify(controller.get())  

@partido_module.post('/')
#@logger
def create_partido():
  return jsonify(controller.create(request.get_json())), 201
  
@partido_module.get('/<string:id>')
def show_partido(id):
  return jsonify(controller.get_by_id(id))

@partido_module.put('/<string:id>')
def update_partido(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@partido_module.delete('/<string:id>')
def delete_partido(id):
  controller.delete(id)
  return jsonify({}), 204
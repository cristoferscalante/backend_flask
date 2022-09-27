from flask import jsonify, request, Blueprint
from controllers.mesas_controller import MesasController
#from decorators.logger_decorator import logger

mesas_module= Blueprint('mesas', __name__)
controller= MesasController()

@mesas_module.get('/')
#@logger
def get_mesas():
  return jsonify(controller.get())  

@mesas_module.post('/')
#@logger
def create_mesas():
  return jsonify(controller.create(request.get_json())), 201
  
@mesas_module.get('/<string:id>')
def show_mesas(id):
  return jsonify(controller.get_by_id(id))

@mesas_module.put('/<string:id>')
def update_mesas(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@mesas_module.delete('/<string:id>')
def delete_mesas(id):
  controller.delete(id)
  return jsonify({}), 204
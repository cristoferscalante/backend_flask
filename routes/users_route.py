import json
from flask import jsonify,request, Blueprint
from controllers.user_controller import UserController
#from decorators.logger_decorator import logger

user_module = Blueprint('users', __name__)
controller = UserController()

@user_module.get('/')
#@logger
def getUsers(): 
    return jsonify(controller.get())

@user_module.get('/<string:id>')
def showUser(id): 
    return jsonify(controller.get_by_key("_id", id))

@user_module.get('/search/<string:key>/<string:value>')
def showUserByCI(key, value): 
    return jsonify(controller.get_by_key(key, value))

@user_module.post('/partidos/<string:partido_id>')
#@logger
def create_user(partido_id):
  return jsonify(controller.create(request.get_json(),partido_id)), 201
  
@user_module.put('/<string:id>')
def update_user(id):
  controller.update(id, request.get_json())
  return jsonify({}), 204
  
@user_module.delete('/<string:id>')
def delete_user(id):
  controller.delete(id)
  return jsonify({}), 204
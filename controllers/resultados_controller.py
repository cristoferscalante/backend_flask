from db.resultados_repository import ResultadosRepository
from db.mesas_repository import MesasRepository
from db.user_repository import UserRepository

from models.resultados_model import ResultadosModel
from models.mesas_model import MesasModel
from models.user_model import UserModel

class ResultadosController():
  
  def __init__(self) -> None:
    self.repo = ResultadosRepository()
    self.repo_mesas = MesasRepository()
    self.repo_user = UserRepository()
  
  def get(self):
      return self.repo.get_all()
  
  def get_by_id(self,id):
    return self.repo.get_by_id(id)
  
  def create(self,data, mesas_id, user_id):
    resultados = ResultadosModel(data)
    user = self.repo_user.get_by_id(user_id) 
    resultados.user = UserModel(user)

    table = self.repo_mesas.get_by_id(mesas_id)
    resultados.table = MesasModel(table)

    return {
      "id": self.repo.save(resultados)
    }
  
  def update(self,id, data):
    resultados = ResultadosModel(data)
    self.repo.update(id, resultados)
  
  def delete(self,id):
    self.repo.delete(id)

  def get_mesas_id(self,  id):
    return self.repo.get_mesas_id(id)

  def get_all_table(self):
    return self.repo.get_all_table()

  def query_groupby(self):
    return self.repo.query_groupby()

  def get_match(self):
    return self.repo.get_match()

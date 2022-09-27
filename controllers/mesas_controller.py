from models.mesas_model import MesasModel
from db.mesas_repository import MesasRepository

class MesasController():
  
  def __init__(self) -> None:
    self.repo = MesasRepository()
  
  def get(self):
      return self.repo.get_all()
  
  def get_by_id(self,id):
    return self.repo.get_by_id(id)
  
  def create(self,data):
    mesas = MesasModel(data)
    #Validate some fields
    return {
      "id": self.repo.save(mesas)
    }
  
  def update(self,id, data):
    mesas = MesasModel(data)
    self.repo.update(id, mesas)
  
  def delete(self,id):
    self.repo.delete(id)
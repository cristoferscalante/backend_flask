from models.partido_model import PartidoModel
from db.partido_repository import PartidoRepository

class PartidoController():
  
  def __init__(self) -> None:
    self.repo = PartidoRepository()
  
  def get(self):
      return self.repo.get_all()
  
  def get_by_id(self,id):
    return self.repo.get_by_key(id)
  
  def create(self,data):
    partido = PartidoModel(data)
    return {
      "id": self.repo.save(partido)
    }
  
  def update(self,id, data):
    partido= PartidoModel(data)
    self.repo.update(id, partido)
  
  def delete(self,id):
    self.repo.delete(id)
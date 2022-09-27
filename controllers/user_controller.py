from db.user_repository import UserRepository
from db.partido_repository import PartidoRepository
from models.partido_model import PartidoModel
from models.user_model import UserModel

class UserController ():

    def __init__(self) -> None:
        self.repo = UserRepository()
        self.repositorio = PartidoRepository()

    def get(self):
        return self.repo.get_all()

    def get_by_key(self, key, value):
        return self.repo.get_by_key(key, value)

    def create(self, data, partido_id):
        user = UserModel(data)
        match = self.repositorio.get_by_id(partido_id)
        user.match = PartidoModel(match)
        return {
            "id": self.repo.save(user)
        }
  
    def update(self,id, data):
        user = UserModel(data)
        self.repo.update(id, user)
  
    def delete(self,id):
        self.repo.delete(id)
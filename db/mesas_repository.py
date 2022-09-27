from db.repository import Repository
from models.mesas_model import MesasModel

class MesasRepository(Repository[MesasModel] ):
  def __init__(self):
    super().__init__()
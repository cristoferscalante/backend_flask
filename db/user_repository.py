from models.user_model import UserModel
from db.repository import Repository

class UserRepository(Repository[UserModel]):
    def __init__(self):
        super().__init__()
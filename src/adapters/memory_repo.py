from src.adapters.repo import AbstractRepository
from src.domain.model import User


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__users = list()

    # GETTERS AND SETTERS
    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name):
        return next((user for user in self.__users if user.user_name == user_name), None)

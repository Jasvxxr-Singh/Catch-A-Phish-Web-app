from src.adapters.repo import AbstractRepository
from src.domain.model import User, Question


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__users = list()
        self.__questions = list()

    # User objects
    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name):
        return next((user for user in self.__users if user.user_name == user_name), None)

    # Question objects
    def add_question(self, question: Question):
        self.__questions.append(question)

    def get_question(self, question_id: int):
        return next((question for question in self.__questions if question.question_id == question_id))

    def get_all_questions(self):
        return self.__questions

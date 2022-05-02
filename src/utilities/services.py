from src.adapters.repo import AbstractRepository
from src.domain.model import User, Question

def get_all_questions(repo: AbstractRepository):
    return repo.get_all_questions()
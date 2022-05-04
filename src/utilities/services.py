from src.adapters.repo import AbstractRepository
from src.domain.model import User, Question

def get_all_questions(repo: AbstractRepository):
    return repo.get_all_questions()

def get_chunks(repo: AbstractRepository, data_array: [], per_page: int):
    return list(repo.chunks(data_array, per_page))
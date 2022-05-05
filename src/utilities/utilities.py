from flask import Blueprint, url_for


import src.adapters.repo as repo
import src.utilities.services as services

utilities_blueprint = Blueprint('utilities_bp', __name__)

def get_all_questions():
    return services.get_all_questions(repo.repo_instance)

def get_chunks(data_array, per_page):
    return services.get_chunks(repo.repo_instance, data_array, per_page)

def get_user_score(user_name):
    return services.get_user_score(repo.repo_instance, user_name)

def update_user_score(user_name, score: int):
    services.update_user_score(repo.repo_instance, user_name, score)


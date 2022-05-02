from flask import Blueprint, url_for

import src.adapters.repo as repo
import src.utilities.services as services

utilities_blueprint = Blueprint('utilities_bp', __name__)

def get_all_questions():
    return services.get_all_questions(repo.repo_instance)
from flask import Blueprint, render_template

quiz_blueprint = Blueprint('quiz_bp', __name__)
@quiz_blueprint.route('/quiz', methods=['GET'])
def quiz():
    return render_template(
        'quiz/quiz.html',
    ) 

from flask import request, session

from flask import Blueprint, render_template

import src.utilities.utilities as utilities
import src.utilities.services as services
import src.adapters.repo as repo

quiz_blueprint2 = Blueprint('quiz_bp2', __name__)
@quiz_blueprint2.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
    q1 = (1, "Someone has successfully phished you"
          )

    q2 = (2, "")

    q3 = (3, "")

    qlist = [q1, q2, q3]

    return render_template(
        'quiz2/module2.html'
        questionlist=qlist,
    )


submit_blueprint2 = Blueprint(submit_bp2, __name__)
@submit_blueprint2.route('/submitquiz2', methods=['POST', 'GET'])
def submit2():
    correct_count = 0
    for question in qlist:
        question_id = str(question.
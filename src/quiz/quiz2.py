from flask import request, session

from flask import Blueprint, render_template

import src.utilities.utilities as utilities
import src.utilities.services as services
import src.adapters.repo as repo

# questions need to be global to be used in submit and quiz2 blueprint
# --------------------------------------------------------------------
q1 = (1, "Someone has successfully phished you")
q2 = (2, "")
q3 = (3, "")
qlist = [q1, q2, q3]
# --------------------------------------------------------------------

quiz_blueprint2 = Blueprint('quiz_bp2', __name__)
@quiz_blueprint2.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
    
    total_number_of_questions = len(qlist)
    question_chunks = utilities.get_chunks(qlist, 1)

    page_number = request.args.get("page_number")

    if page_number is None:
        page_number = 0

    page_number = int(page_number)
    if page_number == 0:
        previous_page = 0
    else:
        previous_page = page_number - 1

    if page_number == len(question_chunks) - 1:
        next_page = len(question_chunks) - 1
    else:
        next_page = page_number + 1


    return render_template(
        'quiz/module2.html',
        questionlist=qlist,
        next_page=next_page,
        prev_page=previous_page,
        total_number_of_questions=total_number_of_questions,
        current_page=page_number,

    )


submit_blueprint2 = Blueprint('submit_bp2', __name__)
@submit_blueprint2.route('/submitquiz2', methods=['POST', 'GET'])
def submit2():
    correct_count = 0

    for question in qlist:
        question_id = str(question.getQ_id())
        print("questionid=", type(question_id))

        selected_option = request.form.get(question_id)
        print("selected_option=", selected_option)
        correct_option = question.get_correct_option()
        print("correct_option=", correct_option)

        if selected_option == correct_option:
            correct_count += 1
        correct_count = str(correct_count)

    return render_template(
        'quiz/result.html',
        quiz_result=correct_count
    )
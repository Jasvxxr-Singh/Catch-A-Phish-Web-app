from flask import request, session

from flask import Blueprint, render_template

import src.utilities.utilities as utilities
from src.domain.model import Question2

q1 = Question2(1,
               "Which one of the statements is correct?",
               "If you get an email that looks like it’s from someone you know you can click on any links as long as you have a spam blocker and anti-virus protection.?",
               " You can trust an email really comes from a client if it uses the client’s logo and contains at least one fact about the client that you know to be true.",
               "statement3",
               "statement4",
               4)
q2 = Question2(1,
               "Which one of the statements is correct?",
               "statement1",
               "statement2",
               "statement3",
               "statement4",
               4)
q3 = Question2(1,
               "Which one of the statements is correct?",
               "statement1",
               "statement2",
               "statement3",
               "statement4",
               4)

qlist = [q1, q2, q3]  # the list stores all the Questions

quiz_blueprint2 = Blueprint('quiz_bp2', __name__)


@quiz_blueprint2.route('/quiz2', methods=['GET', 'POST'])
def quiz2():
    # implements pagination or do we really need it?
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
        num_pages=len(question_chunks),
        current_page=page_number,

    )


submit_blueprint2 = Blueprint("submit_bp2", __name__)


@submit_blueprint2.route('/submitquiz2', methods=['POST', 'GET'])
def submit2():
    correct_count = 0

    for question in qlist:
        question_id = str(question.getQ_id())
        selected_option = request.form.get(question_id)
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count += 1
        correct_count = str(correct_count)

    return render_template(
        # how we want to implement this second part of the quiz
        'quiz/result2.html',
        quiz_result=correct_count
    )

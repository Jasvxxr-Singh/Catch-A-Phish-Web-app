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
               4,
               "this is clearly a phish attack")
q2 = Question2(2,
               "Which one of the statements is correct?",
               "statement1",
               "statement2",
               "statement3",
               "statement4",
               4,
               "this is clearly a phish attack")
q3 = Question2(3,
               "Which one of the statements is correct?",
               "statement1",
               "statement2",
               "statement3",
               "statement4",
               4,
               "this is clearly a phish attack")

qlist = [q1, q2, q3]  # the list stores all the Questions
wrongQ = []


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

    question = qlist[page_number]
    # question = utilities.get_question(page_number + 1)
    score = utilities.get_user_score(session['user_name'])

    return render_template(
        'quiz/module2.html',
        questionlist=qlist,
        question=question,
        next_page=next_page,
        prev_page=previous_page,
        total_questions=total_number_of_questions,
        current_page=page_number,
        q_list=question_chunks[page_number],
        num_pages=len(question_chunks),
        score=score,

    )


submit_blueprint2 = Blueprint("submit_bp2", __name__)


@submit_blueprint2.route('/submitquiz2', methods=['POST', 'GET'])
def submit2():

    total_number_of_questions = len(qlist)
    questions_chunks = utilities.get_chunks(qlist, 1)
    page_number = request.args.get("page_number")

    if page_number is None:
        page_number = 0

    page_number = int(page_number)
    if page_number == 0:
        previous_page = 0
    else:
        previous_page = page_number - 1

    if page_number == len(questions_chunks) - 1:
        next_page = len(questions_chunks) - 1
    else:
        next_page = page_number + 1

    question = qlist[page_number]  # return an object!

    score = utilities.get_user_score(session['user_name'])

    num_emails_left, num_spam, num_legit = (total_number_of_questions - page_number), 5, 5
    correct = False
    selected_option = request.values.get("option")
    correct_option = str(question.get_correct_option())

    if selected_option == correct_option:
        correct = True
    else:
        correct = False
        wrongQ.append(question)

    # Update user score
    if correct: utilities.update_user_score(session['user_name'], 1)

    return render_template(
        'quiz/module2.html',
        results=True,
        quiz_result=correct,
        correct_option=correct_option,

        question=question,
        next_page=next_page,
        prev_page=previous_page,
        total_questions=total_number_of_questions,
        current_page=page_number,
        q_list=questions_chunks[page_number],
        num_pages=len(questions_chunks),
        num_emails_left=num_emails_left, num_spam=num_spam, num_legit=num_legit, score=score
    )


resolutions_blueprint2 = Blueprint('resolutions_bp2', __name__)


@resolutions_blueprint2.route('/resolutions2', methods=['GET'])
def results2():
    return render_template(
        'quiz/resolutions2.html'

    )


solution_blueprint = Blueprint("solution_bp", __name__)


@solution_blueprint.route('/solution', methods=['GET'])
def solution():
    return render_template(
        'quiz/resolutions.html',
        wrong_question=wrongQ

    )

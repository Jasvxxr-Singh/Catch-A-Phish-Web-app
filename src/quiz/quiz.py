from flask import request, session

from flask import Blueprint, render_template, url_for

from src.domain.model import Question
import src.utilities.utilities as utilities
import src.utilities.services as services
import src.adapters.repo as repo

# Temporary Question objects
# format of a Question object = Question(q_id: int, sender_address: str, email_subject: str, email_content: str, is_legitimate: bool, reason: str)
q1 = Question(1,  # the id of the question
               "testaddress1@gmail.com", # sender email address
               "email subject 1", # email subject
               "It looks like your someone has attempted to access your bank account using your password. Please reset" + \
               "your password following the link below:Reset password button links to  https://b775sgH5j4.co/hHjz6Gu",
               False, # False = illegitimate, True = legitimate
               "Urgency in subject. No personalisation in email content. Asks for personal information regarding your bank account - whereas most banks will never ask you to reveal personal information immediately. Website linked in the reset password button has the domain: b775sgH5j4.co which is not a bank related website. ")  # the correct answer
q2 = Question(2,
               "testaddress2@gmail.com",
               "email subject 2", 
               "$2,000 PAK'nSAVE reward! Congratulations, you are a winner!" + \
               "You qualify for a $2,000 PACK'nSAVE reward , this email is Our Official News Letter for your persual." + \
               "Remember, you are one of the only few selected. Registration is only possible for the next 24 " + \
               "hours!",
               False, 
               "Sender email irrelevant to topic on email content. (what can customer service @ certified learn, \".co.UK\" have anything to do with a PAK'n'SAVE reward?). Urgency in subject is often a hint at spam emails. Inconsistent or incorect grammar. Time urgency \"only possible for the next 24 hours\". The registration button actually links to a PDF rather than a website. PDFs can be laced in malicious softward, it is best only to open these if the email is from a certain and trusted sender. ")
q3 = Question(3,
               "testaddress3@gmail.com",
               "email subject 3",
               "Hi, Someone just used your password to sign into your Google Account." + \
               "Information:[insert py dateTime.now][first_name][last_name]" + \
               "Firefox browser Google stopped this sign-in attempt. You should change your password immediately." + \
               "[Change password button links to https://support.google.com-scan78.co.ac/passswipe/245556gysuu7",
               False, 
               "The email google.support isn't actually used by Google. The link in the button actually sends the user to a website discuised as a google domain, but really we can see that the domain is com-scan78.co.ac ")

#questions_list = [q1, q2, q3] - use for testing if necessary

quiz_blueprint = Blueprint('quiz_bp', __name__)
@quiz_blueprint.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions_list = utilities.get_all_questions()
    total_number_of_questions = len(questions_list)
    questions_chunks = utilities.get_chunks(questions_list, 1)

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

    question = questions_list[page_number]


    return render_template(
        'quiz/module1.html',
        question=question,
        next_page=next_page,
        prev_page=previous_page,
        total_questions=total_number_of_questions,
        current_page=page_number,
        q_list=questions_chunks[page_number],
        num_pages=len(questions_chunks),
    )

submit_blueprint = Blueprint('submit_bp', __name__)
@submit_blueprint.route('/submitquiz', methods=['POST', 'GET'])
def submit():
    questions_list = utilities.get_all_questions()
    correct_count = 0
    wrong_questions = []
    for question in questions_list:
        selected_option = request.values.get(str(question.question_id))

        # Find if question is legit or not depending on T/F value of is_legitimate property
        if question.is_legitimate: correct_option = "Legitimate"
        else: correct_option = "Illegitimate"

        if selected_option == correct_option:
            correct_count += 1
        else:
            wrong_questions.append(question.question_id)

    correct_count = str(correct_count)
    if len(wrong_questions) == 0:
        wrong_questions = 0
    return render_template(
        'quiz/result.html',
        quiz_result=correct_count,
        wrong_q=wrong_questions
    )


resolutions_blueprint = Blueprint('resolutions_bp', __name__)
@resolutions_blueprint.route('/resolutions', methods=['GET'])
def results():
    return render_template(
        'quiz/resolutions.html'

    )

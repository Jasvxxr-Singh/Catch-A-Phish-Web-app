from flask import request, session

from flask import Blueprint, render_template

from src.domain.model import Questions

quiz_blueprint = Blueprint('quiz_bp', __name__)
# we add our questions over here

q1 = Questions(1,  # the id of the question
               "It looks like your someone has attempted to access your bank account using your password. Please reset" + \
               "your password following the link below:Reset password button links to  https://b775sgH5j4.co/hHjz6Gu",
               "yes",  # option1
               "No",  # option2
               1)  # the correct answer
q2 = Questions(2,
               "$2,000 PAK'nSAVE reward! Congratulations, you are a winner!" + \
               "You qualify for a $2,000 PACK'nSAVE reward , this email is Our Official News Letter for your persual." + \
               "Remember, you are one of the only few selected. Registration is only possible for the next 24 " + \
               "hours!",
               "yes",
               "NO",
               1)
q3 = Questions(3,
               "Hi, Someone just used your password to sign into your Google Account." + \
               "Information:[insert py dateTime.now][first_name][last_name]" + \
               "Firefox browser Google stopped this sign-in attempt. You should change your password immediately." + \
               "[Change password button links to https://support.google.com-scan78.co.ac/passswipe/245556gysuu7",
               "yes",
               "NO",
               1)

qlist = [q1, q2, q3]


@quiz_blueprint.route('/quiz', methods=['GET'])
def quiz():
    # add the questions here

    return render_template(
        'quiz/module1.html',
        questionlist=qlist,

    )


submit_blueprint = Blueprint('submit_bp', __name__)


@submit_blueprint.route('/submitquiz', methods=['POST', 'GET'])
def submit():
    print('here')
    correct_count = 0
    wrong_questions = []
    for question in qlist:
        question_id = str(question.getQ_id())
        selected_option = request.values.get(question_id)
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count += 1
            # print("correct_count", correct_count)
        else:
            wrong_questions.append(question.getQ_id())

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

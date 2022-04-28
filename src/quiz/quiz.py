from flask import request, session

from flask import Blueprint, render_template

from src.domain.model import Questions

quiz_blueprint = Blueprint('quiz_bp', __name__)
q1 = Questions(1,
               "It looks like your someone has attempted to access your bank account using your password. Please reset" + \
               "your password following the link below:Reset password button links to  https://b775sgH5j4.co/hHjz6Gu",
               "yes",
               "No",
               1)
q2 = Questions(2,
               "$2,000 PAK'nSAVE reward! Congratulations, you are a winner!" + \
               "You qualify for a $2,000 PACK'nSAVE reward , this email is Our Official News Letter for your persual." + \
               "Remember, you are one of the only few selected. Registration is only possible for the next 24 " + \
               "hours!",
               "yes",
               "NO",
               1)

qlist = [q1, q2]


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
    for question in qlist:
        question_id = str(question.getQ_id())
        selected_option = request.values.get(question_id)
        correct_option = question.get_correct_option()
        if selected_option == correct_option:
            correct_count += 1
            print("correct_count", correct_count)
    correct_count = str(correct_count)
    return render_template(
        'quiz/result.html',
        quiz_result=correct_count
    )


resolutions_blueprint = Blueprint('resolutions_bp', __name__)


@resolutions_blueprint.route('/resolutions', methods=['GET'])
def results():
    return render_template(
        'quiz/resolutions.html'
    )

from flask import Blueprint, render_template

from src.domain.model import Questions

quiz_blueprint = Blueprint('quiz_bp', __name__)


@quiz_blueprint.route('/quiz', methods=['GET'])
def quiz():
    que = "It looks like your someone has attempted to access your bank account using your password. Please reset" + \
          "your password following the link below:Reset password button links to  https://b775sgH5j4.co/hHjz6Gu"
    print("1111")
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

    return render_template(
        'quiz/module1.html',
        questionlist=qlist,
        example=que

    )

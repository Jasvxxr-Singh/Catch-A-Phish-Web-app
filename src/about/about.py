from flask import Blueprint, render_template

about_blueprint = Blueprint('about_bp', __name__)
@about_blueprint.route('/about', methods=['GET'])
def about():
    return render_template(
        'about/about.html',
    ) 

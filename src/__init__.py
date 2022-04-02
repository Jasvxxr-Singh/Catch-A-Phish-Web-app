from flask import Flask, render_template
from pathlib import Path


# Import databases or repositories here

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')

    data_path = Path('src') / 'adapters' / 'data'
 
    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .about import about
        app.register_blueprint(about.about_blueprint) 
        
    return app
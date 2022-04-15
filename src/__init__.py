from flask import Flask, render_template
from pathlib import Path

from src.domain.model import User
import src.adapters.repo as repo
from src.adapters.memory_repo import MemoryRepository
from src.adapters import memory_repo, database_repository
from src.adapters.orm import metadata, map_model_to_tables

# SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool

# Import databases or repositories here

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')

    database_uri = app.config['SQLALCHEMY_DATABASE_URI']
    database_echo = app.config['SQLALCHEMY_ECHO']
    database_engine = create_engine(database_uri, connect_args={"check_same_thread": False}, poolclass=NullPool,
                                    echo=database_echo)
    session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)
    repo.repo_instance = database_repository.SqlAlchemyRepository(session_factory)

    if app.config['TESTING'] == 'True' or len(database_engine.table_names()) == 0:
        print("REPOPULATING DATABASE...")

        clear_mappers()
        # create database tables with conditions
        metadata.create_all(database_engine)
        # empty tables
        for table in reversed(metadata.sorted_tables):
            database_engine.execute(table.delete())

        map_model_to_tables()
        #database_mode = True
        #repository_populate.populate(data_path, repo.repo_instance, database_mode)
        #print("REPOPULATING DATABASE... FINISHED")

    else:
        map_model_to_tables()
 
    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .about import about
        app.register_blueprint(about.about_blueprint)

        from .quiz import quiz
        app.register_blueprint(quiz.quiz_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        @app.before_request
        def before_flask_http_request_function():
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.reset_session()

        @app.teardown_appcontext
        def shutdown_session(exception=None):
            if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                repo.repo_instance.close_session()
        
    return app
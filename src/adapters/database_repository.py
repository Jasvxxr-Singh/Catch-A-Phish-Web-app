from typing import List
from flask import _app_ctx_stack
from sqlalchemy import desc, asc
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.sql.expression import asc, text

from src.adapters.repo import AbstractRepository
from src.domain.model import User, Question


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if self.__session is not None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):
    # SESSION MANAGEMENT
    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    # REPOSITORY METHODS
        # USER
    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, user_name: str) -> User:
        user = None
        try:
            user = self._session_cm.session.query(User).filter(User._User__user_name == user_name).one()
        except NoResultFound:
            pass
        return user

    # just to satisfy abstract repository
    def add_question(self, question: Question):
        with self._session_cm as scm:
            scm.session.add(question)
            scm.commit()

    def get_question(self, question_id: int):
        question = None
        try:
            question = self._session_cm.session.query(Question).filter(Question._Question__q_id == question_id).one()
        except NoResultFound:
            pass
        return question

    def get_all_questions(self) -> List[Question]:
        questions = self._session_cm.session.query(Question).all()
        return questions

    def chunks(self, data_array: [], per_page: int):
        if len(data_array) > per_page:
            for i in range(0, len(data_array), per_page):
                yield data_array[i: i + per_page]
        else:
            yield data_array
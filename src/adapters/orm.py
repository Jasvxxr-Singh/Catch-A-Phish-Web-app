from sqlalchemy import (Table, MetaData, Column, Integer, String)
from sqlalchemy.orm import backref, mapper

from src.domain import model

metadata = MetaData()

# TABLE GENERATION
users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)

# MAPPER
def map_model_to_tables():
    mapper(model.User, users_table, properties={
        '_User__user_name': users_table.c.user_name,
        '_User__password': users_table.c.password,
    })
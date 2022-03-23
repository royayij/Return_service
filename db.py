import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

db_user = os.environ["DB_USER"]
db_pass = os.environ["DB_PASS"]
db_addr = os.environ["DB_ADDR"]

engine = sqlalchemy.create_engine(f"postgresql://{db_user}:{db_pass}@{db_addr}:5432/postgres")

if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))
# https://docs.sqlalchemy.org/en/13/orm/session.html
Session = sessionmaker(bind=engine)
# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_url = 'sqlite://mydatabase.db'
engine = create_engine(db_url)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)
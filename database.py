from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # SQLite can't work with threads very good :(
    connect_args={"check_same_thread": False} # So this should be added for SQLite
)

LocalSession = sessionmaker(bind=engine) # make connections to our database engine
Base = declarative_base() # for creating Models


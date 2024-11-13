from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

#SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://@DESKTOP-4MOISVD/COACH_LMS?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://admin:srikar123%23@firstdb.cro480eaysw6.eu-north-1.rds.amazonaws.com/COACH_LMS?driver=ODBC+Driver+17+for+SQL+Server&Connect Timeout=30"

#SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server&Connect Timeout=30"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

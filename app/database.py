from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = settings.fastapi_db_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#if not use SQLAlchemy would need code below
# from datetime import time
# import psycopg2
# from psycopg2.extras import RealDictCursor
# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres",
#                                 password="buster", port=5433, cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print(f"Error: {error}")
#         time.sleep(2)
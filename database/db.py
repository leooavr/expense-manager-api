from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{username}:{password}@localhost/{database}"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

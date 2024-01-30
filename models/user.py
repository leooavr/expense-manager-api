from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    address = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    expense = relationship("Expense", back_populates="user")
    debt = relationship("Debt", back_populates="user")

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password)

    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

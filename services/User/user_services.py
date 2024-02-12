from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from models.user import User
from database.db import get_db
from schemas.user import UserCreate, UserUpdate
from uuid import UUID


class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user(self, db: Session, user_id: UUID):
        user = db.query(User).filter(User.id == user_id).first()
        return user

    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_all_users(self, db: Session):
        return db.query(User).all()

    def create_new_user(self, db: Session, user: UserCreate):
        try:
            hash_password = User.get_password_hash(user.password)
            new_user = User(
                username=user.username,
                password=hash_password,
                email=user.email,
                address=user.address,
                first_name=user.first_name,
                last_name=user.last_name,
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except IntegrityError:
            db.rollback()
            return None

    def update_user_by_id(self, db: Session, user_update: UserUpdate, id: UUID):
        user = self.get_user(db, id)
        if user:
            for attribute, value in user_update.dict().items():
                setattr(user, attribute, value)
            db.commit()
            db.refresh(user)
            return user
        else:
            return False

    def delete_user_by_id(self, db: Session, id: UUID):
        user = self.get_user(db, id)
        if user:
            db.delete(user)
            db.commit()
            return {"message": "User deleted successfully"}
        else:
            return False

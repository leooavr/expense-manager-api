from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate


def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session):
    return db.query(User).all()


def create_new_user(db: Session, user: UserCreate):
    new_password = user.password
    new_user = User(
        username=user.username,
        password=new_password,
        email=user.email,
        address=user.address,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user_by_id(db: Session, user_update: UserUpdate, id: int):
    user = get_user(db, id)
    if user:
        for attribute, value in user_update.dict().items():
            setattr(user, attribute, value)
        db.commit()
        db.refresh(user)
        return user
    else:
        return False


def delete_user_by_id(db: Session, id: int):
    user = get_user(db, id)
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    else:
        return False

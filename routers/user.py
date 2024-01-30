from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.user import User, UserCreate, UserUpdate
from services.User.user_services import UserService

user = APIRouter()
user_service = UserService()


@user.get("/users/", response_model=list[User], tags=["Users"])
def get_users(db: Session = Depends(get_db)):
    users = user_service.get_all_users(db)
    return users


@user.get("/users/{id}", response_model=User, tags=["Users"])
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user.post("/users/", response_model=User, tags=["Users"])
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = user_service.get_user_by_email(db, user.email)
    if new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_new_user(db, user)


@user.put("/users/{id}", response_model=User, tags=["Users"])
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    is_updated = user_service.update_user_by_id(db, user, id)
    if not is_updated:
        raise HTTPException(status_code=404, detail="User not found")
    return is_updated


@user.delete("/users/{id}", tags=["Users"])
def delete_user(id: int, db: Session = Depends(get_db)):
    is_deleted = user_service.delete_user_by_id(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return is_deleted

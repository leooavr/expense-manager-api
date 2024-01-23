from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.user import User, UserCreate, UserUpdate
from database.crud.user import (
    get_all_users,
    get_user,
    create_new_user,
    get_user_by_email,
    delete_user_by_id,
    update_user_by_id,
)

user = APIRouter()


@user.get("/users/", response_model=list[User], tags=["users"])
def get_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    return users


@user.get("/users/{id}", response_model=User, tags=["users"])
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user.post("/users/", response_model=User, tags=["users"])
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = get_user_by_email(db, user.email)
    if new_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_new_user(db, user)


@user.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    is_updated = update_user_by_id(db, user, id)
    if not is_updated:
        raise HTTPException(status_code=404, detail="User not found")
    return is_updated


@user.delete("/users/{id}", tags=["users"])
def delete_user(id: int, db: Session = Depends(get_db)):
    is_deleted = delete_user_by_id(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return is_deleted

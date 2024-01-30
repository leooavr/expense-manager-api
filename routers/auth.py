from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models import User
from schemas import Login, PasswordRecovery
from services.Auth.auth_services import AuthService

auth = APIRouter()
auth_service = AuthService()

@auth.post("/auth/login")
async def login(login_model: Login,db: Session = Depends(get_db)):
    is_login = auth_service.login(login_model,db)
    if not is_login:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login Successful", "user": login_model.username, "access_token": is_login}


@auth.post("/auth/passwordRecovery")
async def password_recovery(password_model: PasswordRecovery,db: Session = Depends(get_db)):
    is_sended = auth_service.password_recovery(password_model,db)
    if not is_sended:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Password sended Successful"}

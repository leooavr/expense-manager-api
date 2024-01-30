from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models import User
from schemas import Login
from services.Auth.auth_services import AuthService

auth = APIRouter()
auth_service = AuthService()

@auth.post("/login")
async def login(login_model: Login,db: Session = Depends(get_db)):
    is_login = auth_service.login(login_model,db)
    if not is_login:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login Successful", "user": login_model.username, "access_token": is_login}

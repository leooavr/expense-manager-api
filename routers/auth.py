from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models import User
from schemas import Login

auth = APIRouter()

@auth.post("/login")
async def login(login_model: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == login_model.username).first()
    if not user or not user.verify_password(login_model.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    # Puedes generar un token JWT o manejar la sesión de otra manera aquí
    return {"message": "Login successful"}

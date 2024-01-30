import jwt
import datetime
from loguru import logger
from fastapi import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database.db import get_db
from services.User.user_services import UserService
from services.Mail.mail_services import MailService
from schemas import Login, PasswordRecovery
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def __init__(
        self,
        user_service: UserService = None,
        mail_service: MailService = None,
        # otp_service: OtpService = None,
    ):
        self.user_service = user_service if user_service is not None else UserService()
        self.mail_service = mail_service if mail_service is not None else MailService()
        # self.otp_service = otp_service if otp_service is not None else OtpService()
        
    def login(self,login_model: Login, db:Session):
        user = self.user_service.get_user_by_username(db,login_model.username)
        if not user or not user.verify_password(login_model.password):
            return False
        jwt_token = self._generate_jwt(user)
        return jwt_token
        
    def _generate_jwt(self, user: User) -> str:
        SECRET_KEY = "your_shared_secret"
        ALGORITHM = "HS256"
        logger.info(f"GENERATING JWT FOR USER {user.username}")
        payload = {
        "sub": str(user.id),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "nbf": datetime.datetime.utcnow(),
        "iat": datetime.datetime.utcnow(),
        }
        jwt_token = jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)
        return jwt_token
    
    def password_recovery(self, password_recovery: PasswordRecovery, db:Session):
        user = self.user_service.get_user_by_email(db,password_recovery.email)
        if user is None:
            return False
        is_sended = self.mail_service.send_password_by_email(user)
        return is_sended
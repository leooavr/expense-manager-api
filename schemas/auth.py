from pydantic import BaseModel
from schemas.expense import Expense
from schemas.debt import Debt


class Login(BaseModel):
    username: str
    password: str


class PasswordRecovery(BaseModel):
    email: str

from pydantic import BaseModel, UUID4
from schemas.expense import Expense
from schemas.debt import Debt


class UserBase(BaseModel):
    username: str
    email: str
    address: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class User(UserBase):
    id: UUID4
    expenses: list[Expense] = []
    debts: list[Debt] = []

    def __init__(self):
        self.expenses = []
        self.debts = []

    class Config:
        from_attributes = True

from pydantic import BaseModel
from typing import Optional
import datetime


class ExpenseBase(BaseModel):
    name: str
    value: int
    pay_date: Optional[datetime.date]
    entity: str
    is_paid: bool
    category: str


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(ExpenseCreate):
    pass


class Expense(ExpenseBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

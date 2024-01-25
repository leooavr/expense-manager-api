from pydantic import BaseModel
from typing import Optional
import datetime


class InstallmentBase(BaseModel):
    number: int
    value: int
    pay_date: Optional[datetime.date]
    is_paid: bool
    debt_id: int


class InstallmentCreate(InstallmentBase):
    pass

class InstallmentUpdate(InstallmentBase):
    pass


class Installment(InstallmentBase):
    id: int
    

    class Config:
        from_attributes = True

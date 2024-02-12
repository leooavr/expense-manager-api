from pydantic import BaseModel, UUID4
from typing import Optional
import datetime


class InstallmentBase(BaseModel):
    number: int
    value: int
    pay_date: Optional[datetime.date]
    is_paid: bool
    debt_id: UUID4


class InstallmentCreate(InstallmentBase):
    pass


class InstallmentUpdate(InstallmentBase):
    pass


class Installment(InstallmentBase):
    id: UUID4

    class Config:
        from_attributes = True

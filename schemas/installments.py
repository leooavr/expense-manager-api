from pydantic import BaseModel
from typing import Optional
import datetime


class InstallmentBase(BaseModel):
    number: int
    value: int
    pay_date: Optional[datetime.date]
    is_paid: bool 
    

class InstallmentCreate(InstallmentBase):
    pass

class Installment(InstallmentBase):
    id: int
    debt_id: int
    
    class Config:
        from_attributes = True
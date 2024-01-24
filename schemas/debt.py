from pydantic import BaseModel
from schemas.installment import Installment


class DebtBase(BaseModel):
    name: str
    value: int
    entity: str
    is_paid: bool
    user_id: int
    debt_collector_id: int


class DebtCreate(DebtBase):
    pass


class DebtUpdate(DebtBase):
    pass


class Debt(DebtBase):
    id: int

    class Config:
        from_attributes = True

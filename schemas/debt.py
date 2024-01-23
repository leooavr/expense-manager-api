from pydantic import BaseModel
from schemas.installments import Installment


class DebtBase(BaseModel):
    name: str
    value: int
    entity: str
    is_paid: bool


class DebtCreate(DebtBase):
    pass


class Debt(DebtBase):
    id: int
    id_user: int

    class Config:
        from_attributes = True

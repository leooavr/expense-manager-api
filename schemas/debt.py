from pydantic import BaseModel, UUID4
from schemas.installment import Installment


class DebtBase(BaseModel):
    name: str
    value: int
    entity: str
    is_paid: bool
    user_id: UUID4
    debt_collector_id: UUID4


class DebtCreate(DebtBase):
    pass


class DebtUpdate(DebtBase):
    pass


class Debt(DebtBase):
    id: UUID4

    class Config:
        from_attributes = True

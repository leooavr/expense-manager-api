from pydantic import BaseModel
from schemas.installment import Installment


class DebtCollectorBase(BaseModel):
    name: str
    category: str


class DebtCollectorCreate(DebtCollectorBase):
    pass


class DebtCollectorUpdate(DebtCollectorBase):
    pass


class DebtCollector(DebtCollectorBase):
    id: int

    class Config:
        from_attributes = True

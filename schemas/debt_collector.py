from pydantic import BaseModel, UUID4
from schemas.installment import Installment


class DebtCollectorBase(BaseModel):
    name: str
    category: str


class DebtCollectorCreate(DebtCollectorBase):
    pass


class DebtCollectorUpdate(DebtCollectorBase):
    pass


class DebtCollector(DebtCollectorBase):
    id: UUID4

    class Config:
        from_attributes = True

import uuid
from sqlalchemy import Column, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Installment(Base):
    __tablename__ = "installments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    number = Column(Integer, index=True)
    value = Column(Integer, index=True)
    pay_date = Column(Date, index=True)
    is_paid = Column(Boolean, index=True)

    debt_id = Column(UUID, ForeignKey("debts.id"))
    debt = relationship("Debt", back_populates="installment")

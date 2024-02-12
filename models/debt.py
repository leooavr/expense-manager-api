import uuid
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Debt(Base):
    __tablename__ = "debts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    value = Column(Integer, index=True)
    entity = Column(String, index=True)
    is_paid = Column(Boolean, index=True)

    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="debt")
    installment = relationship("Installment", back_populates="debt")
    debt_collector_id = Column(UUID, ForeignKey("debt_collectors.id"))
    debt_collector = relationship("DebtCollector", back_populates="debt")

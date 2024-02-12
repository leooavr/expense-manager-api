import uuid
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
from sqlalchemy.dialects.postgresql import UUID


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    value = Column(Integer, index=True)
    pay_date = Column(Date, index=True)
    entity = Column(String, index=True)
    is_paid = Column(Boolean, index=True)
    category = Column(String, index=True)
    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="expense")

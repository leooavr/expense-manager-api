import uuid
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
from sqlalchemy.dialects.postgresql import UUID


class DebtCollector(Base):
    __tablename__ = "debt_collectors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    category = Column(String, index=True)

    debt = relationship("Debt", back_populates="debt_collector")

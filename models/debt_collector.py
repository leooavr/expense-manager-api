from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class DebtCollector(Base):
    __tablename__ = "debt_collectors"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    
    debt = relationship("Debt", back_populates="debt_collector")
    

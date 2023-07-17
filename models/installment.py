from sqlalchemy import Column, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.db import Base

class Installment(Base):
    __tablename__ = "installments"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    number = Column(Integer, index=True)
    value =  Column(Integer, index=True)
    pay_date = Column(Date, index=True)
    paid = Column(Boolean, index=True)
    
    debt_id = Column(Integer, ForeignKey("debts.id"))
    debt = relationship("Debt", back_populates="installment")
    

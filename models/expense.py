from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    value =  Column(Integer, index=True)
    pay_date = Column(Date, index=True)
    entity = Column(String, index=True)
    is_paid = Column(Boolean, index=True)
    category = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="expense")
    
    

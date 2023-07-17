from database.db import Base, engine
from models.user import User
from models.expense import Expense
from models.debt import Debt
from models.installment import Installment
import models

def create_all_tables():
    Base.metadata.create_all(bind=engine)
    return "Tablas creadas satisfactoriamente"
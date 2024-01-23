from database.db import Base, engine
from models import Debt, Installment, DebtCollector, Expense, User

import models


def create_all_tables():
    Base.metadata.create_all(bind=engine)
    return "Tablas creadas satisfactoriamente"

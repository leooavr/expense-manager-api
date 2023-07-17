from sqlalchemy.orm import Session
from models.expense import Expense
from schemas.expense import ExpenseCreate
from database.crud.user import get_user

def get_expense_by_id(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    print(type(expense))
    return expense

def get_all_expenses(db: Session):
    return db.query(Expense).all()

def create_new_expense(db: Session, user_id: int, expense: ExpenseCreate):
    user = get_user(db,user_id)
    new_expense = Expense(name=expense.name,value=expense.value,pay_date=expense.pay_date, entity=expense.entity, paid=False,user_id=user.id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense
   
        
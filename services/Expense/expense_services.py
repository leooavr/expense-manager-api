from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from models.expense import Expense
from database.db import get_db
from schemas.expense import ExpenseCreate, ExpenseUpdate
from services.User.user_services import UserService
from uuid import UUID


class ExpenseService:
    user_service = UserService()

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_expense_by_id(self, db: Session, expense_id: UUID):
        expense = db.query(Expense).filter(Expense.id == expense_id).first()
        print(type(expense))
        return expense

    def get_all_expenses(self, db: Session):
        return db.query(Expense).all()

    def create_new_expense(self, db: Session, user_id: UUID, expense: ExpenseCreate):
        try:
            user = self.user_service.get_user(db, user_id)
            new_expense = Expense(
                name=expense.name,
                value=expense.value,
                pay_date=expense.pay_date,
                entity=expense.entity,
                is_paid=False,
                category=expense.category,
                user_id=user.id,
            )
            db.add(new_expense)
            db.commit()
            db.refresh(new_expense)
            return new_expense
        except IntegrityError:
            db.rollback()
            return None

    def update_expense_by_id(db: Session, expense_update: ExpenseUpdate, id: UUID):
        expense = get_expense_by_id(db, id)
        if expense:
            for attribute, value in expense_update.dict().items():
                setattr(expense, attribute, value)
            db.commit()
            db.refresh(expense)
            return expense
        else:
            return False

    def delete_expense_by_id(db: Session, id: UUID):
        expense = get_expense_by_id(db, id)
        if expense:
            db.delete(expense)
            db.commit()
            return {"message": "Expense deleted successfully"}
        else:
            return False

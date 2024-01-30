from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.expense import Expense, ExpenseCreate, ExpenseUpdate
from services.Expense.expense_services import ExpenseService

expense = APIRouter()
expense_service = ExpenseService()


@expense.get("/expenses/", response_model=list[Expense], tags=["Expenses"])
def get_expenses(db: Session = Depends(get_db)):
    expenses = expense_service.get_all_expenses(db)
    return expenses


@expense.get("/expenses/{id}", response_model=Expense, tags=["Expenses"])
def get_expense(id: int, db: Session = Depends(get_db)):
    expense = expense_service.get_expense_by_id(db, id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@expense.post("/expenses/{user_id}", response_model=Expense, tags=["Expenses"])
def post_expense(expense: ExpenseCreate, user_id: int, db: Session = Depends(get_db)):
    return expense_service.create_new_expense(db, user_id, expense)


@expense.put("/expenses/{id}", response_model=Expense, tags=["Expenses"])
def update_expense(id: int, expense: ExpenseUpdate, db: Session = Depends(get_db)):
    is_updated = expense_service.update_expense_by_id(db, expense, id)
    if not is_updated:
        raise HTTPException(status_code=404, detail="Expense not found")
    return is_updated


@expense.delete("/expenses/{id}", tags=["Expenses"])
def delete_expense(id: int, db: Session = Depends(get_db)):
    is_deleted = expense_service.delete_expense_by_id(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return is_deleted

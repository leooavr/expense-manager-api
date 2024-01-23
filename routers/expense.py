from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.expense import Expense, ExpenseCreate, ExpenseUpdate
from database.crud.expense import (
    get_all_expenses,
    get_expense_by_id,
    create_new_expense,
    update_expense_by_id,
    delete_expense_by_id,
)

expense = APIRouter()


@expense.get("/expenses/", response_model=list[Expense], tags=["Expenses"])
def get_expenses(db: Session = Depends(get_db)):
    expenses = get_all_expenses(db)
    return expenses


@expense.get("/expenses/{id}", response_model=Expense, tags=["Expenses"])
def get_expense(id: int, db: Session = Depends(get_db)):
    expense = get_expense_by_id(db, id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@expense.post("/expenses/{user_id}", response_model=Expense, tags=["Expenses"])
def post_expense(expense: ExpenseCreate, user_id: int, db: Session = Depends(get_db)):
    return create_new_expense(db, user_id, expense)


@expense.put("/expenses/{id}", response_model=Expense, tags=["Expenses"])
def update_expense(id: int, expense: ExpenseUpdate, db: Session = Depends(get_db)):
    is_updated = update_expense_by_id(db, expense, id)
    if not is_updated:
        raise HTTPException(status_code=404, detail="Expense not found")
    return is_updated


@expense.delete("/expenses/{id}", tags=["Expenses"])
def delete_expense(id: int, db: Session = Depends(get_db)):
    is_deleted = delete_expense_by_id(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return is_deleted

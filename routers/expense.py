from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.expense import Expense, ExpenseCreate, ExpenseUpdate
from database.crud.expense import (
    get_all_expenses, 
    get_expense_by_id,
    create_new_expense
)

expense = APIRouter()

@expense.get("/expenses/",response_model=list[Expense], tags=["expenses"])
def get_expenses(db:Session = Depends(get_db)):
    expenses = get_all_expenses(db)
    return expenses


@expense.get("/expenses/{id}",response_model=Expense, tags=["expenses"])
def get_expense(id: int,db:Session = Depends(get_db)):
    expense =get_expense_by_id(db,id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@expense.post("/expenses/{user_id}",response_model=Expense, tags=["expenses"])
def post_expense(expense: ExpenseCreate,user_id:int, db:Session = Depends(get_db)):
    return create_new_expense(db,user_id,expense)

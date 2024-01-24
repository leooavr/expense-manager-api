from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.debt import (
    Debt,
    DebtCreate,
    DebtUpdate,
)
from database.crud.debt import (
    get_debt,
    get_all_debt,
    create_new_debt,
    update_debt_by_id,
    delete_debt_by_id,
)

debt = APIRouter()


@debt.get("/debt/", response_model=list[Debt], tags=["Debts"])
def get_debts(db: Session = Depends(get_db)):
    debts = get_all_debt(db)
    return debts


@debt.get("/debt/{id}", response_model=Debt, tags=["Debts"])
def get_debt_by_id(id: int, db: Session = Depends(get_db)):
    debt = get_debt(db, id)
    if debt is None:
        raise HTTPException(status_code=404, detail="Debt not found")
    return debt


@debt.post("/debt/", response_model=Debt, tags=["Debts"])
def post_debt(debt: DebtCreate, db: Session = Depends(get_db)):
    return create_new_debt(db, debt)


@debt.put("/debt/{id}", response_model=Debt, tags=["Debts"])
def update_debt(id: int, debt: DebtUpdate, db: Session = Depends(get_db)):
    is_updated = update_debt_by_id(db, debt, id)
    if not is_updated:
        raise HTTPException(status_code=404, detail="Debt not found")
    return is_updated


@debt.delete("/debt/{id}", tags=["Debts"])
def delete_debt(id: int, db: Session = Depends(get_db)):
    is_deleted = delete_debt_by_id(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Debt not found")
    return is_deleted

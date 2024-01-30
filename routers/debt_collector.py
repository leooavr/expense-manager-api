from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.debt_collector import (
    DebtCollector,
    DebtCollectorCreate,
    DebtCollectorUpdate,
)
from services.DebtCollector.debt_collector_services import DebtCollectorService

debt_collector = APIRouter()
debt_collector_service = DebtCollectorService()


@debt_collector.get(
    "/debtCollectors/", response_model=list[DebtCollector], tags=["DebtCollectors"]
)
def get_debt_collector(db: Session = Depends(get_db)):
    debt_collectors = debt_collector_service.get_all_debt_collector(db)
    return debt_collectors


@debt_collector.get(
    "/debtCollectors/{id}", response_model=DebtCollector, tags=["DebtCollectors"]
)
def get_debt_collector_by_id(id: int, db: Session = Depends(get_db)):
    debt_collector = debt_collector_service.get_debt_collector(db, id)
    if debt_collector is None:
        raise HTTPException(status_code=404, detail="Debt collector not found")
    return debt_collector


@debt_collector.post(
    "/debtCollectors/", response_model=DebtCollector, tags=["DebtCollectors"]
)
def post_debt_collector(
    debt_collector: DebtCollectorCreate, db: Session = Depends(get_db)
):
    return debt_collector_service.create_new_debt_collector(db, debt_collector)


@debt_collector.put(
    "/debtCollectors/{id}", response_model=DebtCollector, tags=["DebtCollectors"]
)
def update_debt_collector(
    id: int, debt_collector: DebtCollectorUpdate, db: Session = Depends(get_db)
):
    is_updated = debt_collector_service.update_debt_collector_by_id(
        db, debt_collector, id
    )
    if not is_updated:
        raise HTTPException(status_code=404, detail="Debt collector not found")
    return is_updated


@debt_collector.delete("/debtCollectors/{id}", tags=["DebtCollectors"])
def delete_debt_collector(id: int, db: Session = Depends(get_db)):
    is_deleted = debt_collector_service.delete_debt_collector_by_id(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Debt collector not found")
    return is_deleted

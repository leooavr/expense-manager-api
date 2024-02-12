from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from models.debt_collector import DebtCollector
from database.db import get_db
from schemas.debt_collector import DebtCollectorCreate, DebtCollectorUpdate
from uuid import UUID


class DebtCollectorService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_debt_collector(self, db: Session, debt_collector_id: UUID):
        debt_collector = (
            db.query(DebtCollector)
            .filter(DebtCollector.id == debt_collector_id)
            .first()
        )
        return debt_collector

    def get_all_debt_collector(self, db: Session):
        return db.query(DebtCollector).all()

    def create_new_debt_collector(
        self, db: Session, debt_collector: DebtCollectorCreate
    ):
        try:
            new_debt_collector = DebtCollector(
                name=debt_collector.name, category=debt_collector.category
            )
            db.add(new_debt_collector)
            db.commit()
            db.refresh(new_debt_collector)
            return new_debt_collector
        except IntegrityError:
            db.rollback()
            return None

    def update_debt_collector_by_id(
        self, db: Session, debt_collector_update: DebtCollectorUpdate, id: UUID
    ):
        debt_collector = self.get_debt_collector(db, id)
        if debt_collector:
            for attribute, value in debt_collector_update.dict().items():
                setattr(debt_collector, attribute, value)
            db.commit()
            db.refresh(debt_collector)
            return debt_collector
        else:
            return False

    def delete_debt_collector_by_id(self, db: Session, id: UUID):
        debt_collector = self.get_debt_collector(db, id)
        if debt_collector:
            db.delete(debt_collector)
            db.commit()
            return {"message": "Debt collector deleted successfully"}
        else:
            return False

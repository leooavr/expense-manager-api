from sqlalchemy.orm import Session
from models.debt_collector import DebtCollector
from schemas.debt_collector import DebtCollectorCreate, DebtCollectorUpdate


def get_debt_collector(db: Session, debt_collector_id: int):
    debt_collector = (
        db.query(DebtCollector).filter(DebtCollector.id == debt_collector_id).first()
    )
    return debt_collector


def get_all_debt_collector(db: Session):
    return db.query(DebtCollector).all()


def create_new_debt_collector(db: Session, debt_collector: DebtCollectorCreate):
    new_debt_collector = DebtCollector(
        name=debt_collector.name, category=debt_collector.category
    )
    db.add(new_debt_collector)
    db.commit()
    db.refresh(new_debt_collector)
    return new_debt_collector


def update_debt_collector_by_id(
    db: Session, debt_collector_update: DebtCollectorUpdate, id: int
):
    debt_collector = get_debt_collector(db, id)
    if debt_collector:
        for attribute, value in debt_collector_update.dict().items():
            setattr(debt_collector, attribute, value)
        db.commit()
        db.refresh(debt_collector)
        return debt_collector
    else:
        return False


def delete_debt_collector_by_id(db: Session, id: int):
    debt_collector = get_debt_collector(db, id)
    if debt_collector:
        db.delete(debt_collector)
        db.commit()
        return {"message": "Debt collector deleted successfully"}
    else:
        return False

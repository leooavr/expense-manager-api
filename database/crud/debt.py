from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Debt
from schemas.debt import DebtCreate, DebtUpdate


def get_debt(db: Session, debt_id: int):
    debt = db.query(Debt).filter(Debt.id == debt_id).first()
    return debt


def get_all_debt(db: Session):
    return db.query(Debt).all()


def create_new_debt(db: Session, debt: DebtCreate):
    try:
        new_debt = Debt(
            name=debt.name,
            value=debt.value,
            entity=debt.entity,
            is_paid=debt.is_paid,
            user_id=debt.user_id,
            debt_collector_id=debt.debt_collector_id,
        )
        db.add(new_debt)
        db.commit()
        db.refresh(new_debt)
        return new_debt
    except IntegrityError:
        db.rollback()
        return None


def update_debt_by_id(db: Session, debt_update: DebtUpdate, id: int):
    debt = get_debt(db, id)
    if debt:
        for attribute, value in debt_update.dict().items():
            setattr(debt, attribute, value)
        db.commit()
        db.refresh(debt)
        return debt
    else:
        return False


def delete_debt_by_id(db: Session, id: int):
    debt = get_debt(db, id)
    if debt:
        db.delete(debt)
        db.commit()
        return {"message": "Debt deleted successfully"}
    else:
        return False

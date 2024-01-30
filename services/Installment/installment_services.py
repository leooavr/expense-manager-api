from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from models.installment import Installment
from database.db import get_db
from schemas.installment import InstallmentCreate, InstallmentUpdate


class InstallmentService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_installment(self, db: Session, installment_id: int):
        installment = (
            db.query(Installment).filter(Installment.id == installment_id).first()
        )
        return installment

    def get_all_installment(self, db: Session):
        return db.query(Installment).all()

    def create_new_installment(self, db: Session, debt: InstallmentCreate):
        try:
            new_installment = Installment(
                name=debt.name,
                number=debt.number,
                value=debt.value,
                pay_date=debt.pay_date,
                is_paid=debt.is_paid,
                debt_id=debt.debt_id,
            )
            db.add(new_installment)
            db.commit()
            db.refresh(new_installment)
            return new_installment
        except IntegrityError:
            db.rollback()
            return None

    def update_installment_by_id(
        self, db: Session, installment_update: InstallmentUpdate, id: int
    ):
        installment = self.get_installment(db, id)
        if installment:
            for attribute, value in installment_update.dict().items():
                setattr(installment, attribute, value)
            db.commit()
            db.refresh(installment)
            return installment
        else:
            return False

    def delete_installment_by_id(self, db: Session, id: int):
        installment = self.get_installment(db, id)
        if installment:
            db.delete(installment)
            db.commit()
            return {"message": "Installment deleted successfully"}
        else:
            return False

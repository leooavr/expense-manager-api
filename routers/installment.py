from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from schemas.installment import (
    Installment,
    InstallmentCreate,
    InstallmentUpdate,
)
from services.Installment.installment_services import InstallmentService

installment = APIRouter()
installmet_service = InstallmentService()


@installment.get(
    "/installment/", response_model=list[Installment], tags=["Installments"]
)
def get_installments(db: Session = Depends(get_db)):
    installments = installmet_service.get_all_installment(db)
    return installments


@installment.get("/installment/{id}", response_model=Installment, tags=["Installments"])
def get_installment_by_id(id: int, db: Session = Depends(get_db)):
    installment = installmet_service.get_installment(db, id)
    if installment is None:
        raise HTTPException(status_code=404, detail="Installment not found")
    return installment


@installment.post("/installment/", response_model=Installment, tags=["Installments"])
def post_installment(installment: InstallmentCreate, db: Session = Depends(get_db)):
    return installmet_service.create_new_installment(db, installment)


@installment.put("/installment/{id}", response_model=Installment, tags=["Installments"])
def update_installment(
    id: int, installment: InstallmentUpdate, db: Session = Depends(get_db)
):
    is_updated = installmet_service.update_installment_by_id(db, installment, id)
    if not is_updated:
        raise HTTPException(status_code=404, detail="Installment not found")
    return is_updated


@installment.delete("/installment/{id}", tags=["Installments"])
def delete_installment(id: int, db: Session = Depends(get_db)):
    is_deleted = installmet_service.delete_installment_by_id(db, id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail="Installment not found")
    return is_deleted

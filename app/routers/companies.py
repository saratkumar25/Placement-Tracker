from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Company
from app.schemas import CompanyCreate

router = APIRouter(prefix="/companies")


@router.post("/")
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):

    new_company = Company(
        name=company.name,
        location=company.location
    )

    db.add(new_company)
    db.commit()

    return new_company


@router.get("/")
def get_companies(db: Session = Depends(get_db)):

    return db.query(Company).all()
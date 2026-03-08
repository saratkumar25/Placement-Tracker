from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Experience
from app.schemas import ExperienceCreate

router = APIRouter(prefix="/experiences")


@router.post("/")
def create_experience(exp: ExperienceCreate, db: Session = Depends(get_db)):

    new_exp = Experience(
        title=exp.title,
        description=exp.description,
        company_id=exp.company_id,
        user_id=1
    )

    db.add(new_exp)
    db.commit()

    return new_exp


@router.get("/")
def get_experiences(db: Session = Depends(get_db)):

    return db.query(Experience).all()
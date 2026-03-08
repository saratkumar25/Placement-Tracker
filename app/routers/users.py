from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin

from app.auth.password import hash_password, verify_password
from app.auth.jwt_handler import create_token

router = APIRouter(prefix="/users")


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):

    hashed = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        return {"error": "User not found"}

    if not verify_password(user.password, db_user.password):
        return {"error": "Invalid password"}

    token = create_token({"user_id": db_user.id})

    return {"access_token": token}
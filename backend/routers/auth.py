from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

import schemas

from database import SessionLocal
from services.auth_service import register_user, authenticate_user


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/registration", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        created_user = register_user(db, user.login, user.password)
        return created_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        token = authenticate_user(db, user.login, user.password)
        return {"token": token}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

import schemas
from database import SessionLocal
from services.auth_service import get_current_user
from services.user_service import get_user_info

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users/{user_id}", response_model=schemas.UserInfo)
def read_user_info(
    user_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    get_current_user(db, token)
    user_info = get_user_info(db, user_id)
    if not user_info:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

import schemas
from database import SessionLocal
from services.auth_service import get_current_user
from services.email_service import send_feedback_email

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/feedback/")
def send_feedback(
    feedback: schemas.Feedback,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    user = get_current_user(db, token)
    try:
        send_feedback_email(user.login, feedback.title, feedback.description)
        return {"message": "Feedback sent successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to send feedback")

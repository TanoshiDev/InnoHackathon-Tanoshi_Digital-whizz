from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

import schemas

from database import SessionLocal
from services.auth_service import authenticate_user_by_token
from services.comment_service import get_comments_for_post, create_comment


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{post_id}/", response_model=list[schemas.Comment])
def read_comments(post_id: int, db: Session = Depends(get_db)):
    return get_comments_for_post(db, post_id)

@router.post("/{post_id}/", response_model=schemas.Comment)
def add_comment(post_id: int, comment: schemas.CommentCreate, token: str, db: Session = Depends(get_db)):
    try:
        user = authenticate_user_by_token(db, token)
        return create_comment(db, post_id, user.ID, comment.text, comment.parent_id)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

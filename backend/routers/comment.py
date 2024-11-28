from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

import schemas
from database import SessionLocal
from services.auth_service import get_current_user
from services.comment_service import get_comments_for_post, create_comment

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{post_id}/", response_model=List[schemas.Comment])
def read_comments(post_id: int, db: Session = Depends(get_db)):
    return get_comments_for_post(db, post_id)


@router.post("/{post_id}/", response_model=schemas.Comment)
def add_comment(
    post_id: int,
    comment: schemas.CommentCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    user = get_current_user(db, token)
    return create_comment(db, post_id, user.ID, comment.text, comment.parent_id)

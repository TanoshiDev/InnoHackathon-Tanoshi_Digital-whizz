import schemas
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

from database import SessionLocal

from services.theme_service import get_all_posts, get_post_by_id, like_post, create_post, search_posts
from services.auth_service import authenticate_user_by_token


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Post])
def read_themes(limit: int = 100, token: Optional[str] = None, db: Session = Depends(get_db)):
    user_id = None
    if token:
        user = authenticate_user_by_token(db, token)
        user_id = user.ID
    return get_all_posts(db, user_id, limit)

@router.get("/{post_id}", response_model=schemas.Post)
def read_theme(post_id: int, token: Optional[str] = None, db: Session = Depends(get_db)):
    user_id = None
    if token:
        user = authenticate_user_by_token(db, token)
        user_id = user.ID
    try:
        return get_post_by_id(db, post_id, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=schemas.Post, tags=["Themes"])
def create_theme(post: schemas.PostCreate, token: str, db: Session = Depends(get_db)):
    try:
        user = authenticate_user_by_token(db, token)
        return create_post(db, post.topic, post.title, post.text, user.ID)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/{post_id}/like", response_model=schemas.Post)
def like_theme(post_id: int, token: str, db: Session = Depends(get_db)):
    user = authenticate_user_by_token(db, token)
    try:
        return like_post(db, post_id, user.ID)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/search/themes", response_model=list[schemas.Post])
def search_themes(query: str, limit: int = 100, db: Session = Depends(get_db)):
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    return search_posts(db, query, limit)

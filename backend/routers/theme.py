from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

import schemas
from database import SessionLocal
from services.theme_service import (
    get_all_posts,
    get_post_by_id,
    like_post,
    create_post,
    search_posts,
    get_posts_by_category,
)
from services.auth_service import get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.Post])
def read_themes(
    limit: int = 100, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user = get_current_user(db, token)
    return get_all_posts(db, user.ID, limit)


@router.get("/{post_id}", response_model=schemas.Post)
def read_theme(
    post_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user = get_current_user(db, token)
    try:
        return get_post_by_id(db, post_id, user.ID)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=schemas.Post)
def create_theme(
    post: schemas.PostCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    user = get_current_user(db, token)
    try:
        return create_post(db, post.topic, post.title, post.text, user.ID)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{post_id}/like", response_model=schemas.Post)
def like_theme(
    post_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user = get_current_user(db, token)
    try:
        return like_post(db, post_id, user.ID)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/search/themes", response_model=List[schemas.Post])
def search_themes(
    query: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user = get_current_user(db, token)
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    return search_posts(db, query)


@router.get("/category/{category}", response_model=List[schemas.Post])
def get_themes_by_category(
    category: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user = get_current_user(db, token)
    try:
        return get_posts_by_category(db, category, user.ID)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

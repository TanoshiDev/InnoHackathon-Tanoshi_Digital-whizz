from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

import models


def get_all_posts(db: Session, user_id: Optional[int] = None, limit: int = 100):
    posts = db.query(models.Post).order_by(models.Post.date.desc()).limit(limit).all()
    if user_id is not None:
        for post in posts:
            post.user_liked = user_liked_post(db, post.ID, user_id) is not None
    return posts

def get_post_by_id(db: Session, post_id: int, user_id: Optional[int] = None):
    post = db.query(models.Post).filter(models.Post.ID == post_id).first()
    if not post:
        raise ValueError("Post not found")
    if user_id is not None:
        post.user_liked = user_liked_post(db, post.ID, user_id) is not None
    else:
        post.user_liked = False
    return post

def user_liked_post(db: Session, post_id: int, user_id: int):
    return db.query(models.Like).filter(models.Like.post_id == post_id, models.Like.user_id == user_id).first()

def add_like(db: Session, post_id: int, user_id: int):
    if user_liked_post(db, post_id, user_id):
        raise ValueError("User already liked this post")
    new_like = models.Like(post_id=post_id, user_id=user_id)
    post = db.query(models.Post).filter(models.Post.ID == post_id).first()
    post.likes += 1
    db.add(new_like)
    db.commit()
    db.refresh(post)
    return post

def create_post(db: Session, topic: str, title: str, text: str, author_id: int):
    db_post = models.Post(topic=topic, title=title, text=text, author_id=author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def search_posts(db: Session, query: str, limit: int = 100):
    keywords = query.split()
    filters = [or_(models.Post.title.ilike(f"%{word}%"), models.Post.text.ilike(f"%{word}%")) for word in keywords]
    return db.query(models.Post).filter(and_(*filters)).order_by(models.Post.date.desc()).limit(limit).all()

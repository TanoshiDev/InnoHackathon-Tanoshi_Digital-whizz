from typing import Optional
from sqlalchemy.orm import Session

import repositories.post_repository as post_repo


def get_all_posts(db: Session, user_id: Optional[int] = None, limit: int = 100):
    return post_repo.get_all_posts(db, user_id, limit)

def get_post_by_id(db: Session, post_id: int, user_id: Optional[int] = None):
    return post_repo.get_post_by_id(db, post_id, user_id)

def like_post(db: Session, post_id: int, user_id: int):
    try:
        return post_repo.add_like(db, post_id, user_id)
    except ValueError as e:
        raise ValueError(str(e))

def create_post(db: Session, topic: str, title: str, text: str, author_id: int):
    return post_repo.create_post(db, topic, title, text, author_id)

def search_posts(db: Session, query: str, limit: int = 100):
    return post_repo.search_posts(db, query, limit)

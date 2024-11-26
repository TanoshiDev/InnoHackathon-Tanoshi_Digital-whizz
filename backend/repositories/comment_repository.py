from sqlalchemy.orm import Session

import models


def get_comments_for_post(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()

def create_comment(db: Session, post_id: int, user_id: int, text: str, parent_id: int = None):
    db_comment = models.Comment(post_id=post_id, user_id=user_id, text=text, parent_id=parent_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

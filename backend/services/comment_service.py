from sqlalchemy.orm import Session

import repositories.comment_repository as comment_repo


def get_comments_for_post(db: Session, post_id: int):
    return comment_repo.get_comments_for_post(db, post_id)


def create_comment(
    db: Session, post_id: int, user_id: int, text: str, parent_id: int = None
):
    return comment_repo.create_comment(db, post_id, user_id, text, parent_id)

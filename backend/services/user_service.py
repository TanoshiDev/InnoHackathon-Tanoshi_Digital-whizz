from sqlalchemy.orm import Session

import schemas
from repositories.user_repository import get_user_by_id


def get_user_info(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        user_info = schemas.UserInfo.from_orm(user)
        if user.avatar:
            user_info.avatar = f"/users/{user.ID}/avatar"
        return user_info
    return None

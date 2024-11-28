from sqlalchemy.orm import Session

import models


def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.ID == user_id).first()


def create_user(db: Session, login: str, password: str):
    db_user = models.User(login=login, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

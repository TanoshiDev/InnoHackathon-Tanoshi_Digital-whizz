from sqlalchemy.orm import Session

import models


def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()

def get_user_by_token(db: Session, token: str):
    return db.query(models.User).filter(models.User.token == token).first()

def create_user(db: Session, login: str, password: str, token: str):
    db_user = models.User(login=login, password=password, token=token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

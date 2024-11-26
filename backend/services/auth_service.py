import uuid

from sqlalchemy.orm import Session
from passlib.context import CryptContext

import models

import repositories.user_repository as user_repo


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(db: Session, login: str, password: str):
    existing_user = user_repo.get_user_by_login(db, login)
    if existing_user:
        raise ValueError("Login already registered")
    
    hashed_password = pwd_context.hash(password)
    token = str(uuid.uuid4())
    return user_repo.create_user(db, login, hashed_password, token)

def authenticate_user(db: Session, login: str, password: str):
    user = user_repo.get_user_by_login(db, login)
    if not user or not pwd_context.verify(password, user.password):
        raise ValueError("Invalid login or password")
    return user.token

def authenticate_user_by_token(db: Session, token: str):
    print(f"Authenticating token: {token}")  
    user = db.query(models.User).filter(models.User.token == token).first()
    if not user:
        print(f"Token not found in database: {token}")  
        raise ValueError("Invalid token")
    print(f"Authenticated user: {user.login}, ID: {user.ID}") 
    return user

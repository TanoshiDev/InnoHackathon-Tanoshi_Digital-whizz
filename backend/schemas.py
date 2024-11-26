from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    login: str

class UserCreate(BaseModel):
    login: str
    password: str

class User(UserBase):
    ID: int
    token: str
    avatar: Optional[str] = None

    class Config:
        from_attributes = True

class PostBase(BaseModel):
    topic: str
    title: str
    text: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    ID: int
    author_id: int
    date: datetime
    likes: int
    user_liked: Optional[bool] = None

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    text: str
    parent_id: Optional[int] = None

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    ID: int
    post_id: int
    user_id: int
    date: datetime

    class Config:
        from_attributes = True

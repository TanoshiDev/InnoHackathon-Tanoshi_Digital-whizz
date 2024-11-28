from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    login: str


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    ID: int
    login: str
    avatar: Optional[str] = None

    class Config:
        from_attributes = True


class UserInfo(BaseModel):
    ID: int
    login: str
    avatar: Optional[str] = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: Optional[str] = None


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


class Feedback(BaseModel):
    title: str
    description: str

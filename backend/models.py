from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    func,
    Text,
)
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    ID = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String)
    avatar = Column(String, nullable=True)

    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    ID = Column(Integer, primary_key=True, index=True)
    topic = Column(String)
    title = Column(String)
    text = Column(Text)
    author_id = Column(Integer, ForeignKey("users.ID"))
    date = Column(DateTime(timezone=True), server_default=func.now())
    likes = Column(Integer, default=0)

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    likes_rel = relationship("Like", back_populates="post")


class Comment(Base):
    __tablename__ = "comments"

    ID = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.ID"))
    user_id = Column(Integer, ForeignKey("users.ID"))
    text = Column(Text)
    parent_id = Column(Integer, ForeignKey("comments.ID"), nullable=True)
    date = Column(DateTime(timezone=True), server_default=func.now())

    post = relationship("Post", back_populates="comments")
    user = relationship("User", back_populates="comments")
    replies = relationship("Comment", remote_side=[ID])


class Like(Base):
    __tablename__ = "likes"

    ID = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.ID"))
    user_id = Column(Integer, ForeignKey("users.ID"))

    post = relationship("Post", back_populates="likes_rel")
    user = relationship("User", back_populates="likes")

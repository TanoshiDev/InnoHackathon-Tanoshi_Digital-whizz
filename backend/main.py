from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine
from routers import auth, theme, comment, avatar, user, feedback

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(theme.router, prefix="/themes", tags=["Themes"])
app.include_router(comment.router, prefix="/comments", tags=["Comments"])
app.include_router(avatar.router, tags=["Avatar"])
app.include_router(user.router, tags=["User"])
app.include_router(feedback.router, tags=["Feedback"])

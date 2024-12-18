from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import FileResponse

from database import SessionLocal
from services.avatar_service import AvatarService
from services.auth_service import get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/avatar")
def upload_avatar(
    file: UploadFile,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    user = get_current_user(db, token)
    return AvatarService.save_avatar(user.ID, file, db)


@router.get("/users/{user_id}/avatar")
def get_avatar(user_id: int, db: Session = Depends(get_db)):
    avatar_path = AvatarService.get_avatar(user_id, db)
    return FileResponse(avatar_path)

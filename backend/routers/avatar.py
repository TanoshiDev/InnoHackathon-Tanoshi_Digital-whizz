from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from fastapi import APIRouter, UploadFile, HTTPException, Depends, Header

from database import SessionLocal
from services.avatar_service import AvatarService
from services.auth_service import authenticate_user_by_token


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/avatar")
def upload_avatar(file: UploadFile, token: str = Header(None), db: Session = Depends(get_db)):
    if not token:
        raise HTTPException(status_code=401, detail="Token is missing")

    user = authenticate_user_by_token(db, token)
    
    return AvatarService.save_avatar(user.ID, file, db)

@router.get("/users/{user_id}/avatar")
def get_avatar(user_id: int, db: Session = Depends(get_db)):
    avatar_path = AvatarService.get_avatar(user_id, db)
    return FileResponse(avatar_path)

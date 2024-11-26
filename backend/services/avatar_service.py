import os

from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException

import models


class AvatarService:
    UPLOAD_DIR = "uploads/avatars"

    @staticmethod
    def save_avatar(user_id: int, file: UploadFile, db: Session):
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Uploaded file is not an image")

        os.makedirs(AvatarService.UPLOAD_DIR, exist_ok=True)

        user = db.query(models.User).filter(models.User.ID == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        if user.avatar:
            old_avatar_path = os.path.join(AvatarService.UPLOAD_DIR, user.avatar)
            if os.path.exists(old_avatar_path):
                os.remove(old_avatar_path)

        file_extension = file.filename.split(".")[-1]
        new_filename = f"user_{user_id}.{file_extension}"
        file_path = os.path.join(AvatarService.UPLOAD_DIR, new_filename)

        with open(file_path, "wb") as f:
            f.write(file.file.read())

        user.avatar = new_filename
        db.commit()
        db.refresh(user)

        return {"avatar_url": f"/users/{user_id}/avatar"}

    @staticmethod
    def get_avatar(user_id: int, db: Session):
        user = db.query(models.User).filter(models.User.ID == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.avatar:
            raise HTTPException(status_code=404, detail="Avatar not found")

        return os.path.join(AvatarService.UPLOAD_DIR, user.avatar)

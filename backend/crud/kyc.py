from sqlalchemy.orm import Session
from backend.models.user import User
from fastapi import UploadFile

def upload_kyc_documents(db: Session, id: int, aadhaar: UploadFile, pan: UploadFile) -> bool:
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        return False
    db_user.kyc_status = 'in_progress' # Simulate upload process
    db.commit()
    return True

def check_kyc_status(db: Session, id: int) -> str:
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        return False
    return db_user.kyc_status
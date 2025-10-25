from sqlalchemy.orm import Session
from backend.models.user import User
from backend.models.kyc_documents import KYC_Documents
from fastapi import UploadFile

def upload_kyc_documents(db: Session, id: int, aadhaar: UploadFile, pan: UploadFile) -> bool:
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        return False
    
    kyc_doc = KYC_Documents(user_id=id)
    db.add(kyc_doc)
        
    kyc_doc.aadhaar = aadhaar.file.read()
    kyc_doc.pan = pan.file.read()
    
    db_user.kyc_status = 'in_progress'
    db.commit()
    return True

def check_kyc_status(db: Session, id: int) -> str:
    db_user = db.query(User).filter(User.id == id).first()
    if not db_user:
        return False
    return db_user.kyc_status
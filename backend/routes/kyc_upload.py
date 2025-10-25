from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from backend.schemas.user import UserResponse
from backend.auth import get_current_user
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.crud.kyc import upload_kyc_documents

router = APIRouter()

@router.post("/kyc-upload")
def kyc_upload(aadhaar: UploadFile = File(...), pan: UploadFile = File(...), user: UserResponse = Depends(get_current_user),
               db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    if not upload_kyc_documents(db, user.id, aadhaar, pan):
        raise HTTPException(status=500, detail="Failed to upload KYC documents")
    
    return {"message": "KYC documents uploaded successfully"}
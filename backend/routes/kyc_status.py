from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.user import UserResponse
from backend.auth import get_current_user
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.crud.kyc import check_kyc_status

router = APIRouter()

@router.post("/kyc-status")
def kyc_upload(user: UserResponse = Depends(get_current_user), db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    status = check_kyc_status(db, user.id)
    if not status:
        HTTPException(status_code=500, detail="Could not retrieve KYC status")
        
    return {"kyc_status": status}
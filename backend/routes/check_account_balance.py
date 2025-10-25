from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.user import UserResponse
from backend.auth import get_current_user
from backend.crud.account import get_account_by_number
from sqlalchemy.orm import Session
from backend.db import get_db

router = APIRouter()

@router.post("/check-account-balance")
def signin(account_number: str, pin: int, user: UserResponse = Depends(get_current_user),db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    account = get_account_by_number(db, account_number)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    if account.pin != pin:
        raise HTTPException(status_code=403, detail="Invalid PIN")
    
    return {
        f"Your account balance is {account.balance}"
    }
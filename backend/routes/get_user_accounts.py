from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.account import AccountResponse
from backend.schemas.user import UserResponse
from backend.auth import get_current_user
from backend.crud.user import get_user_by_id
from backend.crud.account import get_accounts_by_user
from sqlalchemy.orm import Session
from backend.db import get_db

router = APIRouter()

@router.post("/get-user-accounts", response_model=list[AccountResponse])
def signin(user: UserResponse = Depends(get_current_user),db: Session = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    accounts = get_accounts_by_user(db, user.id)
    return accounts
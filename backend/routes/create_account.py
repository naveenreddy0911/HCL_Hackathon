from fastapi import APIRouter, Depends, HTTPException
from backend.schemas.account import AccountCreate
from backend.schemas.user import UserResponse
from backend.auth import get_current_user
from backend.crud.user import get_user_by_id
from backend.crud.account import create_account
from sqlalchemy.orm import Session
from backend.db import get_db

router = APIRouter()

@router.post("/create-account")
def signin(
    account: AccountCreate,
    user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    new_account = create_account(db, user.id, account)
    return {
        "message": "Account created successfully",
        "account_number": new_account.account_number
    }
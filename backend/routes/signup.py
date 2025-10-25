from fastapi import APIRouter, Depends, HTTPException
from backend.crud.user import create_user, get_user_by_email
from backend.schemas.user import UserSignup
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import create_access_token

router = APIRouter()

@router.post("/signup")
def signin(user: UserSignup, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = create_user(db=db, user=user)
    if not new_user:
        raise HTTPException(status_code=401)
    
    access_token = create_access_token(data={"user_id": new_user.id})
    return {
        "access_token": access_token
    }
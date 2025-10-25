from fastapi import APIRouter, Depends, HTTPException
from backend.crud.user import create_user
from backend.schemas.user import UserSignup
from sqlalchemy.orm import Session
from backend.db import get_db

router = APIRouter()

@router.post("/signup")
def signin(user: UserSignup, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    if not db_user:
        raise HTTPException(status_code=401)
    
    return {
        "message": "Account created"
    }
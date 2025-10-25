from fastapi import APIRouter, Depends, HTTPException
from backend.crud.user import authenticate_user
from backend.schemas.user import UserSignin
from sqlalchemy.orm import Session
from backend.db import get_db

router = APIRouter()

@router.post("/signin")
def signin(user: UserSignin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user)
    if not db_user:
        raise HTTPException(status_code=401, detail="Email or password didn't match")
    
    return {
        "message": "Your are now signed in"
    }
from fastapi import APIRouter, Depends, HTTPException
from backend.crud.user import authenticate_user
from backend.schemas.user import UserSignin
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import create_access_token

router = APIRouter()

@router.post("/signin")
def signin(user: UserSignin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user)
    if not db_user:
        raise HTTPException(status_code=401, detail="Email or password didn't match")
    
    access_token = create_access_token(data={"user_id": db_user.id})
    return {
        "access_token": access_token
    }
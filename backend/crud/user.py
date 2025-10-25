from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserSignin, UserSignup

def create_user(db: Session, user: UserSignup):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user: UserSignin):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or db_user.password!=user.password:
        return False
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()
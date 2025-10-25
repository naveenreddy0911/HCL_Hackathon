from sqlalchemy.orm import Session
from backend.models.user import User
from backend.schemas.user import UserSignin, UserSignup
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"])

def create_user(db: Session, user: UserSignup):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(name=user.name,email=user.email,password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user: UserSignin):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        return False
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()
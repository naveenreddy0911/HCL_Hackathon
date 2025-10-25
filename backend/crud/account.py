from sqlalchemy.orm import Session
from backend.models.account import Account
from backend.schemas.account import AccountCreate
import secrets

def generate_account_number(db: Session) -> str:
    while True:
        number = str(secrets.randbelow(9000000000) + 1000000000)
        if not db.query(Account).filter(Account.account_number == number).first():
            return number

def create_account(db: Session, user_id: int, account: AccountCreate):
    account_number = generate_account_number(db)
    db_account = Account(
        user_id=user_id,
        account_type=account.account_type.value,
        account_number=account_number,
        pin=account.pin,
        balance=5000
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_account_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def get_account_by_number(db: Session, account_number: str):
    return db.query(Account).filter(Account.account_number == account_number).first()

def get_accounts_by_user(db: Session, user_id: int):
    return db.query(Account).filter(Account.user_id == user_id).all()
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from backend.db import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account_number = Column(String(12), unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    account_type = Column(Enum('savings', 'current', 'fd', name="account_type"))
    balance = Column(Integer, default=5000)
    pin = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    user = relationship("User", back_populates="accounts")
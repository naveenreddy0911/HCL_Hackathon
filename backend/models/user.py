from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from backend.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    kyc_status = Column(Enum('pending', 'in_progress', 'completed', name="kyc_status"), default='pending')
    
    kyc_documents = relationship("KYC_Documents", back_populates="user")
    accounts = relationship("Account", back_populates="user")
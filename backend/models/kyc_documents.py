from sqlalchemy import Column, Integer, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.db import Base

class KYC_Documents(Base):
    __tablename__ = "kyc_documnets"
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    aadhaar = Column(LargeBinary)
    pan = Column(LargeBinary)
    uploaded_at = Column(DateTime, server_default=func.now())
    
    user = relationship("User", back_populates="kyc_documents")
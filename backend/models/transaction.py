# from sqlalchemy import Column, Integer, Enum, DateTime, String, ForeignKey
# from sqlalchemy.sql import func
# from backend.db import Base
# from sqlalchemy.orm import relationship

# class Transaction(Base):
#     __tablename__ = "transactions"
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     transaction_type = Column(Enum('deposit', 'withdrawal', 'transfer', name="transaction_type"))
#     user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#     account_number = Column(String)
    
#     receiver_user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
#     receiver_account_number = Column(String, nullable=True)
#     amount = Column(Integer, nullable=False)
#     timestamp = Column(DateTime, server_default=func.now())
    
#     user = relationship("User", back_populates="transactions")
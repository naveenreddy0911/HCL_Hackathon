# from pydantic import BaseModel, conint
# from datetime import datetime
# from typing import Annotated
# from enum import Enum

# Ammount = Annotated[int, conint(gt=0)]
# Pin = Annotated[int, conint(ge=1000, le=9999)]

# class TransactionType(str, Enum):
#     deposit = 'deposit'
#     withdrawal = 'withdrawal'
#     transfer = 'transfer'

# class DepositRequest(BaseModel):
#     account_number: int
#     amount: Ammount

# class WithdrawalRequest(BaseModel):
#     account_number: int
#     amount: Ammount
#     pin: Pin

# class TransferRequest(BaseModel):
#     from_account_number: int
#     to_account_number: int
#     amount: Ammount
#     pin: Pin
    
# class TransactionResponse(BaseModel):
#     transaction_id: int
#     account_number: int
#     amount: Ammount
#     transaction_type: TransactionType
#     timestamp: datetime

#     class Config:
#         from_attributes = True
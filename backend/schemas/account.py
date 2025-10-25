from pydantic import BaseModel, conint
from typing import Annotated
from enum import Enum

Balance = Annotated[int, conint(ge=0)]
Pin = Annotated[int, conint(ge=1000, le=9999)]

class AccountType(str, Enum):
    savings = 'savings'
    current = 'current'
    fd = 'fd'

class AccountBase(BaseModel):
    account_type: AccountType
    account_number: str
    balance: Balance
    
class AccountCreate(BaseModel):
    account_type: AccountType
    pin: Pin
    
class AccountResponse(AccountBase):
    class ConfigDict:
        from_attributes = True
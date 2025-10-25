from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserSignup(UserBase):
    password: str

class UserSignin(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserSignup(UserBase):
    password: str

class UserSignin(BaseModel):
    email: EmailStr
    password: str
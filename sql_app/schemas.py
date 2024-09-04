from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    name: str
    surname: str
    dateOfBirth: date
    weight: int
    height: int
    email: EmailStr

class UserCreate(UserBase):
    password: str
class LoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

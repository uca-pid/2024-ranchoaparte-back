from pydantic import BaseModel, Field
from datetime import datetime

# Modelo para registrar un nuevo Food
class UserRegister(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    weight: float = Field(..., ge=0)
    height: float = Field(..., ge=0)
    birthDate: datetime 
class UserForgotPassword(BaseModel):
    email: str
class UserLogin(BaseModel):
    email: str
    password: str
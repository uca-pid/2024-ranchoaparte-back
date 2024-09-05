from sqlalchemy.orm import Session
from .models import User,Code
from .schemas import UserCreate
from passlib.context import CryptContext
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(name=user.name, surname=user.surname, dateOfBirth=user.dateOfBirth,weight= user.weight,height= user.height, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_reset_code(db: Session,email: str ,reset_code:str):
    db_reset_code_withExpDate = Code(email = email,reset_code= reset_code, status = "1", expired_in= datetime.now() )
    db.add(db_reset_code_withExpDate)
    db.commit()
    db.refresh(db_reset_code_withExpDate)
    return db_reset_code_withExpDate


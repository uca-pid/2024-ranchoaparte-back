from sqlalchemy import Column, Integer, String, create_engine,Date,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./login.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname= Column(String, index=True)
    dateOfBirth = Column(Date,index=True)
    weight = Column(Integer, index=True)
    height = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

Base.metadata.create_all(bind=engine)

class Code(Base):
   __tablename__ = "py_codes"
   id = Column(Integer, primary_key=True, index=True)
   email= Column(String, index=True)
   reset_code = Column(String, index=True)
   status= Column(String(1), index=True)
   expired_in = Column(DateTime, index=True)

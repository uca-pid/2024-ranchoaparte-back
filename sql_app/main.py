from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base
from . import crud,  schemas
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext

Base.metadata.create_all(bind=engine)

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    try:
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        return crud.create_user(db=db, user=user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))

@app.post("/users/login")
def login(login_request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=login_request.email)
    if user and pwd_context.verify(login_request.password, user.hashed_password):
        return {"success": True}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")
@app.get("/users/{user_id}", response_model=schemas.UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base
from . import crud,  schemas,security,email
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
import uuid

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

@app.post("/forgot-Password")
async def forgot_password(request: schemas.ForgotPassword,db: Session = Depends(get_db)):
    #check the user existis
    result =  crud.get_user_by_email(db, email=request.email)
    if not result:
        raise HTTPException(status_code=404, detail= 'User not found.')
    
    #create reset code and save 
    reset_code= str(uuid.uuid1())
    crud.create_reset_code(db ,request.email,reset_code) 

    #send the mail
    subjet = "Your Password reset Code"
    recip= [request.email]
    message = """
    <!DOCTYPE html>
    <html>
        <a href= "http://http://localhost:3000/ResetPassword?reset_password_token={1:}" a>
    </html>
        """.format(request.email,reset_code)
    
    await email.send_email(subjet,recip,message)

    return {
        "code":200,
        "message" : "we've sent an email instructions to reset"
    }
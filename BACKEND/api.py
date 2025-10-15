# backend/main.py

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker,  Session
from sqlalchemy.ext.declarative import declarative_base
from argon2 import PasswordHasher


# --- Database setup ---
DATABASE_URL = "mssql+pyodbc://COLLINS-PC\\SQLEXPRESS/AMYDB?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# --- User Table ---
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=False)
    password = Column(String)
    is_active = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# --- Pydantic Schemas ---
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

# --- FastAPI App ---
app = FastAPI()

# --- Password Hashing ---
ph = PasswordHasher()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# --- Signup Route ---
@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if not user.username.strip() or not user.password.strip():
        raise  HTTPException(status_code=400, detail="provide Username and Password.")
    
    existing_user = db.query(User).filter(User.username == user.username).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists.")
    
    hased_pw = ph.hash(user.password)
    new_user = User(username=user.username, password=hased_pw)
    db.add(new_user)
    db.commit()
    
    return {"message": "User created successfully. Please log in."}


# --- Login Route ---
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(User.username == user.username).first()
    
    if not existing_user or not ph.verify(existing_user.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    
    # Mark user as active on successful login
    existing_user.is_active = True
    db.commit()
    return {"message": "Login successful", "user": {"username": existing_user.username, "is_active": existing_user.is_active}}


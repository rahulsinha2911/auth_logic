# # main.py
# from fastapi import FastAPI, Depends, HTTPException, Security
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from sqlalchemy import Column, Integer, String, create_engine, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy.exc import IntegrityError
# from passlib.context import CryptContext
# from jose import JWTError, jwt
# from typing import Optional
# import os
# from datetime import datetime, timedelta
# import random
# from fastapi.staticfiles import StaticFiles


# # Database setup
# DATABASE_URL = "sqlite:///./users.db"
# Base = declarative_base()
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # JWT configuration
# SECRET_KEY = "your_secret_key"  # Change this to a random secret key
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # Models
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     api_key = Column(String, unique=True)
#     credits = Column(Float, default=0.0)

# Base.metadata.create_all(bind=engine)

# # FastAPI app
# app = FastAPI()
# app.mount("/static", StaticFiles(directory="frontend"), name="static")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Password hashing functions
# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

# # JWT token functions
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=401,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     db = SessionLocal()
#     user = db.query(User).filter(User.username == username).first()
#     if user is None:
#         raise credentials_exception
#     return user

# # User registration
# @app.post("/register/")
# async def register(username: str, password: str, db: Session = Depends(get_db)):
#     hashed_password = hash_password(password)
#     api_key = f"api_key_{random.randint(1000, 9999)}"
#     user = User(username=username, hashed_password=hashed_password, api_key=api_key)
#     db.add(user)
#     try:
#         db.commit()
#         db.refresh(user)
#     except IntegrityError:
#         db.rollback()
#         raise HTTPException(status_code=400, detail="Username already registered")
#     return {"api_key": user.api_key}

# # User login
# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
#     return {"access_token": access_token, "token_type": "bearer"}

# # Deduct credits
# @app.post("/deduct_credits/")
# async def deduct_credits(amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     if current_user.credits < amount:
#         raise HTTPException(status_code=400, detail="Not enough credits")
#     current_user.credits -= amount
#     db.commit()
#     return {"credits_remaining": current_user.credits}

# # Add credits (for testing)
# @app.post("/add_credits/")
# async def add_credits(amount: float, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     current_user.credits += amount
#     db.commit()
#     return {"credits": current_user.credits}

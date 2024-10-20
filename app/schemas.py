from pydantic import BaseModel, EmailStr
from fastapi import Form

class UserCreate(BaseModel):
    username: str
    email: EmailStr  # Added email field
    password: str

class User(BaseModel):
    id: int
    username: str
    email: EmailStr  # Added email field
    credits: float

    class Config:
        orm_mode = True

class APIKeyCreate(BaseModel):
    user_id: int

class APIKey(BaseModel):
    id: int
    key: str
    user_id: int

    class Config:
        orm_mode = True

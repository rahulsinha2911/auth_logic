from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserInDB(UserCreate):
    hashed_password: str
    api_key: str
    credits: float

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password
import random


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    api_key = f"api_key_{random.randint(1000, 9999)}"
    db_user = models.User(username=user.username, hashed_password=hashed_password, api_key=api_key)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

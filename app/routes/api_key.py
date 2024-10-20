import secrets
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api_key", response_model=schemas.APIKey)
def create_api_key(api_key_data: schemas.APIKeyCreate, db: Session = Depends(get_db)):
    api_key = secrets.token_hex(16)
    db_api_key = models.APIKey(key=api_key, user_id=api_key_data.user_id)
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)
    return db_api_key

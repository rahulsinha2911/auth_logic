from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models
from ..business_logic import business_logic

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/use_credits")
def use_credits(api_key: str, cost: float, params: int, db: Session = Depends(get_db)):
    db_api_key = db.query(models.APIKey).filter(models.APIKey.key == api_key).first()
    if not db_api_key:
        raise HTTPException(status_code=400, detail="Invalid API key")

    user = db_api_key.owner
    if user.credits < cost:
        raise HTTPException(status_code=400, detail="Insufficient credits")

    user.credits -= cost
    result = business_logic(params)  # Call the business logic function
    db.commit()
    return {"remaining_credits": user.credits, "result": result}

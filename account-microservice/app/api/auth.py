from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.auth import authenticate_user, create_access_token
from core.database import get_db

router = APIRouter()

@router.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

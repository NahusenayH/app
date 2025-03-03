from fastapi import APIRouter, Depends, Security
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    token = await AuthService.create_user(db, user)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = await AuthService.authenticate_user(db, form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}
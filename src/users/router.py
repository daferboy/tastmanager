from fastapi import APIRouter, status, Depends
from src.users.dtos import UserSchema, UserResponseSchema
from sqlalchemy.orm import Session
from src.utils.database import get_db
from src.users import controller

user_routes = APIRouter(prefix="/users")

@user_routes.post("/register", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def register(data:UserSchema, db:Session = Depends(get_db)):
    return controller.register(data,db)

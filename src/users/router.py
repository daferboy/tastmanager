from fastapi import APIRouter, status, Depends, Request
from src.users.dtos import UserSchema, UserResponseSchema, LoginSchema
from sqlalchemy.orm import Session
from src.utils.database import get_db
from src.users import controller

user_routes = APIRouter(prefix="/users")

@user_routes.post("/register", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def register(data:UserSchema, db:Session = Depends(get_db)):
    return controller.register(data,db)

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(credentials: LoginSchema, db: Session = Depends(get_db)):
    return controller.login(credentials, db)

@user_routes.get("/isAuth", status_code=status.HTTP_200_OK)
def isauthenticated(request:Request, db:Session = Depends(get_db)):
    return controller.isauthenticated(request, db)
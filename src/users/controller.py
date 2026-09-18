from src.users.dtos import UserSchema
from sqlalchemy.orm import Session
from src.users.model import User

def register(data: UserSchema, db:Session):
    print(data)
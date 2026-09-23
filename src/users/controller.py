from fastapi import HTTPException, status
from src.users.dtos import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from src.users.model import User
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def register(data: UserSchema, db:Session):
   #1. User validation
   is_username = db.query(User).filter(data.username == User.username).first()
   if is_username:
      raise HTTPException(404,f"Username {data.username} already exists...")

   #2. Email Validation
   is_email = db.query(User).filter(data.email == User.email).first()
   if is_email:
      raise HTTPException(404, f"Email {data.email} already exists...")

   hash_password = get_password_hash(data.password)
    
   user = User(
      name = data.name,
      username = data.username,
      password = hash_password,
      email = data.email
   )

   db.add(user)
   db.commit()
   db.refresh(user)

   return user

def login(credentials:LoginSchema, db:Session):
   user = db.query(User).filter(credentials.username == User.username).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized username")
   return "Done"
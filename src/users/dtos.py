from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str

class UserResponseSchema(BaseModel):
    id: int
    name: str
    username: str
    password: str
    email: str
    createdAt: datetime

class LoginSchema(BaseModel):
    username: str
    password: str
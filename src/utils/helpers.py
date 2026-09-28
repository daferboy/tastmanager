from fastapi import Request,status, HTTPException, Depends
from sqlalchemy.orm import Session
from src.utils.settings import settings
from src.users.model import User
import jwt
from jwt.exceptions import InvalidTokenError
from src.utils.database import get_db

def isauthenticated(request:Request, db:Session = Depends(get_db)):
   try:
      token = request.headers['authorization']
      if not token:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Expired...")

      # print(request.headers['authorization'])
      token = (request.headers['authorization'])
      token = token.split(" ")[-1]
      # print(token)
      data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
      # print(data)
      user_id = data["_user_id"]
      # exp_time = data["exp"]

      # current_time = datetime.now().timestamp()

      # if current_time > exp_time:
      #    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Time Out...")

      user = db.query(User).filter(User.id == user_id).first()
      if not user:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User ID...")

      return user 
   except InvalidTokenError:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Expired...")
   
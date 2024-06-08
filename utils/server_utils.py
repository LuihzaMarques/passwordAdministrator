from config.db import conn
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def database_user_verification(username, password):
    for x in conn.local.user.find({}, {"_id": 0, "name": 0}):
        if username == x["user"] and password == x["password"]:
            return True

    return False

def authenticate_user(credentials:HTTPBasicCredentials = Depends(security)):
  if not database_user_verification(credentials.username, credentials.password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication credentials",
      headers={"WWW-Authenticate": "Basic"},
    )
  
  return True
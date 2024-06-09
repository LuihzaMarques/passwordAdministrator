from utils.db_utils import database_user_verification
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def authenticate_user(credentials:HTTPBasicCredentials = Depends(security)):
  if not database_user_verification(credentials.username, credentials.password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication credentials",
      headers={"WWW-Authenticate": "Basic"},
    )
  
  return True
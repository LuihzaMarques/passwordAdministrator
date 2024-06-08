from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from config.db import conn
from schemas.user import userEntity, usersEntity, userPasswordDescription, usersPasswordDescription
from models.user import ResponseStatus, User, Password 
from utils.password_utils import generate_password
from utils.server_utils import verificacao_usuario_banco

user = APIRouter()
security = HTTPBasic()

def autenticar_usuario(credentials:HTTPBasicCredentials = Depends(security)):
  if not verificacao_usuario_banco(credentials.username, credentials.password):
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid authentication credentials",
      headers={"WWW-Authenticate": "Basic"},
    )
  
  return True

@user.get("/users")
async def find_all_users():
  return usersEntity(conn.local.user.find())

@user.post("/users")
async def create_user(user:User, verification = Depends(autenticar_usuario)):
  new_user = dict(user)

  if "id" in new_user:
    del new_user["id"]

  password = generate_password()
  new_user["password"] = password

  id = conn.local.user.insert_one(new_user).inserted_id

  user_from_db = conn.local.user.find_one({"_id": id})

  user_from_db["password"] = password
  user_from_db["id"] = str(id) 

  return userEntity(user_from_db)

@user.get("/generate_new_password", response_model=ResponseStatus)
async def generate_new_password(verification = Depends(autenticar_usuario)):
  password = generate_password()
  data = {"password": password}
  response_status = ResponseStatus(data=data, path="/generate_password")

  return response_status

@user.post("/request_password", response_model=ResponseStatus)
async def request_password(user:str, password:str, desc:str, verification = Depends(autenticar_usuario)):
  password = generate_password()
  data = {"password": password}
  response_status = ResponseStatus(data=data, path="/request_password")

  return response_status
   
@user.get("/list_passwords_description")
async def list_passwords_description():
  return usersPasswordDescription(conn.local.user.find())

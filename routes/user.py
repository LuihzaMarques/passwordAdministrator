from fastapi import APIRouter, Depends
from config.db import conn
from schemas.user import userEntity, usersEntity, userPasswordDescription, usersPasswordDescription
from models.user import ResponseStatus, User, Password 
from utils.password_utils import generate_password
from utils.server_utils import authenticate_user

user = APIRouter()

@user.get("/users")
async def find_all_users():
  return usersEntity(conn.local.user.find())

@user.post("/users")
async def create_user(user:User, verification = Depends(authenticate_user)):
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
async def generate_new_password(verification = Depends(authenticate_user)):
  password = generate_password()
  data = {"password": password}
  response_status = ResponseStatus(data=data, path="/generate_password")

  return response_status

@user.post("/request_password", response_model=ResponseStatus)
async def request_password(user:str, password:str, desc:str, verification = Depends(authenticate_user)):
  password = generate_password()
  data = {"password": password}
  response_status = ResponseStatus(data=data, path="/request_password")

  return response_status
   
@user.get("/list_passwords_description")
async def list_passwords_description():
  return usersPasswordDescription(conn.local.user.find())

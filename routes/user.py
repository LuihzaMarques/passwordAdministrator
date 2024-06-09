from fastapi import APIRouter, Depends
from config.db import conn
from schemas.user import user_entity
from models.user import ResponseStatus, User, Password 
from utils.password_utils import generate_password
from utils.server_utils import authenticate_user
from utils.db_utils import list_all_users, list_all_user_passwords, create_user_db

user = APIRouter()

@user.get("/users")
async def find_all_users():
  return list_all_users()

@user.post("/users")
async def create_user(user:User):
  new_password = generate_password()
  new_user_db = create_user_db(user, new_password)
  return user_entity(new_user_db)

@user.get("/generate_new_password", response_model=ResponseStatus)
async def generate_new_password(description_password:str, verification = Depends(authenticate_user)):
  password = generate_password()

  data = {"password": password, "description": description_password}
  response_status = ResponseStatus(data=data, path="/generate_new_password")

  return response_status

@user.post("/request_password", response_model=ResponseStatus)
async def request_password(password:str, description_password:str, verification = Depends(authenticate_user)):
  password = generate_password()
  data = {"password": password, "description": description_password}
  response_status = ResponseStatus(data=data, path="/request_password")

  return response_status
   
@user.get("/list_all_passwords_created")
async def list_all_passwords_created():
  return list_all_user_passwords()

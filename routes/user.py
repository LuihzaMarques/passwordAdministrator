from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity, userPasswordDescription, usersPasswordDescription
from models.user import ResponseStatus, User, Password 
from utils.password_utils import generate_password

user = APIRouter()

@user.get('/users')
def find_all_users():
  return usersEntity(conn.local.user.find())

@user.post("/users")
def create_user(user:User):

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

@user.get("/generate_password", response_model=ResponseStatus)
async def genetate_password(user:str, password:str):
    password = generate_password()

    data = {"password": password}
    response_status = ResponseStatus(data=data, path="/generate_password")

    return response_status

@user.post("/request_password", response_model=ResponseStatus)
async def request_password(user:str, password:str, desc:str):
   
   password = generate_password()
   data = {"password": password}
   response_status = ResponseStatus(data=data, path="/request_password")

   return response_status
   
@user.get("/list_passwords_description")
def list_passwords_description ():
  return usersPasswordDescription(conn.local.user.find())
    
    




from config.db import conn
from schemas.user import users_list

def list_all_users():
  return users_list(conn.local.user.find())

def list_all_user_passwords():
  count_password = conn.local.user.count_documents({})
  return {"total_passwords": count_password}

def create_user_db(user, password):
  new_user = dict(user)

  if "id" in new_user:
    del new_user["id"]

  new_user["password"] = password
  id = conn.local.user.insert_one(new_user).inserted_id
  user_from_db = conn.local.user.find_one({"_id": id})

  user_from_db["password"] = password
  user_from_db["id"] = str(id)

  return user_from_db

def database_user_verification(username, password):
  for x in conn.local.user.find({}, {"_id": 0, "name": 0}):
    if username == x["user"] and password == x["password"]:
      return True

  return False
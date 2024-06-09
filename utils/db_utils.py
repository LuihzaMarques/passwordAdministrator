from config.db import conn
from schemas.user import users_list, users_password_description

def list_all_users():
  return users_list(conn.local.user.find())

def list_all_user_passwords():
  count_password = conn.local.user.count_documents({})
  return {"total_passwords": count_password}

def database_user_verification(username, password):
  for x in conn.local.user.find({}, {"_id": 0, "name": 0}):
    if username == x["user"] and password == x["password"]:
      return True

  return False
from config.db import conn
from schemas.user import usersEntity

def list_all_users():
  return usersEntity(conn.local.user.find())

def database_user_verification(username, password):
  for x in conn.local.user.find({}, {"_id": 0, "name": 0}):
    if username == x["user"] and password == x["password"]:
      return True

  return False
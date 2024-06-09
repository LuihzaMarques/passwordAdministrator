def user_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "user": item["user"],
        "password": item["password"]
    }

def users_entity(entity) -> list:
    return[user_entity(item) for item in entity]

def user_list(item) -> dict:
    return {"user": item["user"]}

def users_list(entity) -> list:
    return[user_list(item) for item in entity]

def user_password_description(item: dict) -> dict:
    return {
      #  "description" : item["description"],
        "password": item["password"]
    }

def users_password_description(entity) -> list:
    return[user_password_description(item) for item in entity]
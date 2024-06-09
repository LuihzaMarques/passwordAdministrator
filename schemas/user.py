def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "user": item["user"],
        "password": item["password"]
    }


def usersEntity(entity) -> list:
      return[userEntity(item) for item in entity]


def userPasswordDescription(item: dict) -> dict:
    return {
      #  "description" : item["description"],
        "password": item["password"]
    }


def usersPasswordDescription(entity) -> list:
      return[userPasswordDescription(item) for item in entity]
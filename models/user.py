from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    #id: Optional[str]
    name : str
    user : str 
   #password : str 

class Password(BaseModel):
    password: str
    description: str

passwords: List[Password] = []


class ResponseStatus(BaseModel):
    statusCode: int = 200
    data: dict = {}
    called_at: datetime = datetime.now()
    path: str

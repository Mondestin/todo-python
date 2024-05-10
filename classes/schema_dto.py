import datetime
from pydantic import BaseModel

# Model Pydantic = Datatype
class Todo(BaseModel):
    id: str
    name: str

# No ID for Todo requests 
class TodoNoID(BaseModel):
    name: str

# No ID for User requests 
class User(BaseModel):
    email: str
    password: str  
   
    
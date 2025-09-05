from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    isActive: bool


inputData = {
    'name':"Harsh Verma",
    'age':22,
    "isActive":True
}

user = User(**inputData)
print(user)






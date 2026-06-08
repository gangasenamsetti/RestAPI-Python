# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
# name: str
# age: int

# @app.post("/users/")
# async def create_user(user: User):
# return {"name": user.name, "age": user.age}



from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

class Demo(BaseModel):
    name: str
    age: int

    @field_validator("age")
    
    def check_age(cls, v):
        if v <= 18:
            raise ValueError("age must be greater than 18")
        return v

@app.post("/users/")
async def create_user(user: Demo):
    u={"name": user.name, "age": user.age}
    return u

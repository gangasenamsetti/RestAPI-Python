from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def first():
    return {"Hi":"fastapi"}

@app.get("/items/")
def second():
    return {"Returning":"Items"}

#To post the data
#put and delete takes path parameter
@app.post("/items/")
def create_item(name:str,price:float):
    return {"name":"price"}

#To update the data
@app.put("/items/{item_id}")
def update_item(item_id:int,name:str,price:float):
    return {"item_id":item_id,"name":name,"price":price}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {"message":f"item {item_id} deleted succesfuly"}

#path parameters
# @app.get("/users/{user_id}")
# def get_user(user_id:int):
# return {"user":user_id}

#query parameters
@app.get("/users/")
def get_user(user_id:int,name:str):
    return {"user":user_id,"name":name}


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/users/")
# async def create_user(user: User):
#     return {"name": user.name, "age": user.age}

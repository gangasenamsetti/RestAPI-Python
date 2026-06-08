# from fastapi import FastAPI
# import uvicorn
# from pydantic import BaseModel
# app=FastAPI()

# class Student(BaseModel):
#     id:int
#     name:str

# data={
#     'id':1,
#     'name': "ganga"
# }

# s1=Student(**data)
# print(s1)
# print(s1.model_dump())

# from fastapi import FastAPI
# import uvicorn
# from pydantic import BaseModel,Field
# app=FastAPI()

# @app.get("/student")
# class Student(BaseModel):
#    id:int
#    name:str
# async def fun(s:Student):
#    return {s.id,s.name}

# from fastapi import FastAPI
# import uvicorn
# from pydantic import BaseModel,Field
# app=FastAPI()

# @app.get("/profile")
# class Profile(BaseModel):
#    name:str=Field(...,min_length=0,max_length=10)
#    technology:str

# async def fun(p:Profile):
#    return {p.name,p.technology}

# if __name__ == "__main__":
#    uvicorn.run("pydantic_basic:app", host="127.0.0.1", port=8080, reload=True)


from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI()

class Profile(BaseModel):
    name: str = Field(..., min_length=1, max_length=10)
    technology: str

@app.get("/profile")
async def get_details(name: str, technology: str):
    return {
        "name": name,
        "technology": technology
    }

@app.post("/profile")
async def post_details(p:Profile):
    return p

@app.post("/student")
async def student_details(name:str,percentage:int):
    return {
        "name":name,
        "percentage":percentage
    }


if __name__ == "__main__":
    uvicorn.run("pydantic_basic:app",host="127.0.0.1",port=8080,reload=True)



import uvicorn
from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# async def hello():
#    return {"message": "Hello World1"}

@app.get("/world/{name}/{age}")
async def helloo(name:str,age:int):
   return {"name": "hello"+" "+name,"age": "age"}

# @app.get("/world")
# async def helloo():
#    return "hello world welcome to fastAPI"

#path parameter
@app.get("/{color}/{type}")
async def mobile(color:str,type:str):
   return {"color": color, "type":type}

if __name__ == "__main__":
   uvicorn.run("hello:app", host="127.0.0.1", port=8000, reload=True)


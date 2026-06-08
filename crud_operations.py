from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

data = []

class Books(BaseModel):
    id: int
    author: str
    price: int

@app.post("/books")
async def post_details(b: Books):
    data.append(b.model_dump())
    return data

@app.get("/books")
async def get_details(id:int):
    return data[id-1]

@app.put("/books")
async def modify_details(id:int,b:Books):
    data[id-1] = b
    return data

@app.delete("/books")
async def delete_details(id:int):
    data.pop(id-1)
    return data
if __name__ == "__main__":
    uvicorn.run("crud_operations:app", host="127.0.0.1", port=8080, reload=True)

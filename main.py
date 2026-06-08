import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app1= FastAPI()

class User(BaseModel):
    id:int
    name:str
    age:int


class Employee(BaseModel):
    id:int
    age:int
    name:str

#Routing 
@app1.get('/')
def read_root():
    return {"Hello":"Ganga"}

@app1.get('/items')
def list_items():
    #return {"car":"Toyota","Year":"2019"}
    return {"fruits":["apple","orange"]}


user=User(id=1,name="Chinni",age=22)
@app1.get('/Employ')
def employee_details():
    e=Employee(id=1,age=22,name="Nishank")
    return e



if __name__ == "__main__":
   uvicorn.run("main:app1", host="127.0.0.1", port=8080, reload=True)

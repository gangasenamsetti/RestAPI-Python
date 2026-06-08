from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Person(BaseModel):
    id:int
    first_name:str
    last_name:str
    age:int

ll=[]

@app.post("/person_details")
def create_person(p:Person):
    ll.append(p)
    return {f"person {p} created successfully"}

@app.get("/person_details")
def get_details():
    return ll




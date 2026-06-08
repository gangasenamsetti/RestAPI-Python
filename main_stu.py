from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import logging
import time

from database import get_db,engine
import database
from models import Student, Base
from data_layer import (
    create_student, get_all_students, get_student_by_id,
    update_student, delete_student
)
from pydantic import BaseModel
from typing import List, Optional

import uvicorn

# Initialize FastAPI app
app = FastAPI()
database.Base.metadata.create_all(engine)

# ----------------- Logging Configuration -----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a"
)

# ----------------- Pydantic Schemas -----------------
class StudentCreate(BaseModel):
    name: str
    age: int
    grade: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    grade: Optional[str]

    class Config:
        orm_mode = True

# ----------------- Middleware -----------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logging.info(
        f"{request.method} {request.url.path} - {response.status_code} - {duration:.4f}s"
    )
    return response

# ----------------- Exception Handlers -----------------
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logging.error(f"HTTPException: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

# ----------------- Routes -----------------

@app.post("/students/", response_model=StudentResponse, status_code=201)
def create_student_api(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)

@app.get("/students/", response_model=List[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_all_students(db)

@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student_api(student_id: int, updates: StudentUpdate, db: Session = Depends(get_db)):
    student = update_student(db, student_id, updates)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.delete("/students/{student_id}", response_model=dict)
def delete_student_api(student_id: int, db: Session = Depends(get_db)):
    student = delete_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

# ----------------- Run the App -----------------
if __name__ == "__main__":
    uvicorn.run("main_stu:app", host="127.0.0.1", port=8000, reload=True)

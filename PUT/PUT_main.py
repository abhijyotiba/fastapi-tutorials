from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="PUT Method Tutorial",
    description="Fully update student data by ID.",
    version="1.0.0"
)

# Simulated database
db: Dict[int, dict] = {
    1: {"name": "Alice", "subject": "Math"},
    2: {"name": "Bob", "subject": "Science"}
}

class Student(BaseModel):
    name: str
    subject: str

@app.put("/students/{student_id}", tags=["PUT"])
def update_student(student_id: int, updated_data: Student):
    """
    Fully replaces a student's data.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db[student_id] = updated_data.dict()
    return {"message": "Student updated successfully", "data": db[student_id]}

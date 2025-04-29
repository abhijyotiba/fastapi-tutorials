from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI(
    title="PATCH Method Tutorial",
    description="Partially update student data by ID.",
    version="1.0.0"
)

# Simulated database
db: Dict[int, dict] = {
    1: {"name": "Alice", "subject": "Math"},
    2: {"name": "Bob", "subject": "Science"}
}

class PartialStudent(BaseModel):
    name: Optional[str] = None
    subject: Optional[str] = None

@app.patch("/students/{student_id}", tags=["PATCH"])
def partial_update_student(student_id: int, updated_fields: PartialStudent):
    """
    Partially updates specific fields of a student's data.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    update_data = updated_fields.dict(exclude_unset=True)
    db[student_id].update(update_data)
    
    return {"message": "Student partially updated", "data": db[student_id]}

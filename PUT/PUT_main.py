from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(
    title="PUT, PATCH & DELETE Method Tutorial",
    version="1.0.0",
    description="Examples for update and delete operations using FastAPI."
)

# -----------------------------
# 🗃️ In-memory 'Database'
# -----------------------------

db: Dict[int, dict] = {
    1: {"name": "Alice", "subject": "Math"},
    2: {"name": "Bob", "subject": "Science"}
}

# -----------------------------
# 📄 Pydantic Models
# -----------------------------

class Student(BaseModel):
    name: str
    subject: str

class PartialStudent(BaseModel):
    name: Optional[str] = None
    subject: Optional[str] = None

# -----------------------------
# ✏️ PUT Method - Replace Entire Resource
# -----------------------------

@app.put("/students/{student_id}", tags=["PUT"])
def update_student(student_id: int, updated_data: Student):
    """
    Fully replace a student's data.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db[student_id] = updated_data.dict()
    return {"message": "Student updated successfully", "data": db[student_id]}

# -----------------------------
# 🛠 PATCH Method - Partial Update
# -----------------------------

@app.patch("/students/{student_id}", tags=["PATCH"])
def partial_update_student(student_id: int, updated_fields: PartialStudent):
    """
    Partially update a student's data.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    current_data = db[student_id]
    update_data = updated_fields.dict(exclude_unset=True)
    
    current_data.update(update_data)
    db[student_id] = current_data
    
    return {"message": "Student partially updated", "data": db[student_id]}

# -----------------------------
# ❌ DELETE Method - Remove Resource
# -----------------------------

@app.delete("/students/{student_id}", tags=["DELETE"])
def delete_student(student_id: int):
    """
    Delete a student by ID.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    deleted = db.pop(student_id)
    return {"message": "Student deleted", "deleted_data": deleted}

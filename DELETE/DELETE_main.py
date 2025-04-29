from fastapi import FastAPI, HTTPException
from typing import Dict

app = FastAPI(
    title="DELETE Method Tutorial",
    description="Delete a student record by ID.",
    version="1.0.0"
)

# Simulated database
db: Dict[int, dict] = {
    1: {"name": "Alice", "subject": "Math"},
    2: {"name": "Bob", "subject": "Science"}
}

@app.delete("/students/{student_id}", tags=["DELETE"])
def delete_student(student_id: int):
    """
    Deletes a student from the database.
    """
    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")
    
    deleted = db.pop(student_id)
    return {"message": "Student deleted", "deleted_data": deleted}

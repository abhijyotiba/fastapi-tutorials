from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
import csv

app = FastAPI(
    title="POST Method Tutorial",
    version="1.0.0",
    description="API for submitting form and contact data via POST requests."
)

# -----------------------------------
# 📄 Models
# -----------------------------------

class Info(BaseModel):
    name: str
    roll_no: int
    subject: str
    phone: Optional[int] = None


class Contact(BaseModel):
    name: str
    email: EmailStr
    message: str

# -----------------------------------
# 📝 Endpoints
# -----------------------------------

@app.post("/form", tags=["Form Submission"])
def get_info(form: Info):
    """
    Accepts student info and returns it.
    
    Parameters:
    - name: str
    - roll_no: int
    - subject: str
    - phone: Optional[int]
    """
    return {"message": "This is your info", "data": form}


@app.post("/contact", tags=["Forms"])
def contact_form(data: Contact):
    """
    Accepts contact data and saves it to a CSV file.
    
    Parameters:
    - name: str
    - email: EmailStr
    - message: str
    """
    if not data.email:
        raise HTTPException(status_code=400, detail="Email is required.")
    
    save_to_csv(data)
    
    return {
        "status": "success",
        "message": f"Thank you {data.name}, we received your message!",
        "your_email": data.email
    }

# -----------------------------------
# 💾 Utility Functions
# -----------------------------------

def save_to_csv(data: Contact):
    """
    Save contact form data to a CSV file.
    """
    with open('contact_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data.name, data.email, data.message])

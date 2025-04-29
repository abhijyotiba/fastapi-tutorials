from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , EmailStr 
from typing import Optional
import csv 

app = FastAPI( title= 'CRUD OPERATION' , version ='1.0.0')

class Contact(BaseModel):
    name : str
    phone : int
    email : EmailStr
    address : Optional[str] = None
    
class BasicInfo(Contact):
    roll_no : int
    std : int
    classteacher : str

def save_to_csv(data):
    with open('contact_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data.name, data.phone, data.email , data.address])

temp_database =[] 

# Operation = CREATE
@app.post('/contact' , tags=['CREATE'])
async def submit_contact(data : Contact):
    save_to_csv(data)
    temp_database.append(data)
    
    return {
        "message": f"Hello {data.name}!! Thank you for submitting your information.",
        "name": data.name,
        "phone": data.phone,
        "email": data.email,
        "address": data.address
    }

        
# Operation = GET
@app.get('/contact/all' , tags=['REQUEST'])
async def get_info():
    return temp_database

@app.get('/contact/{item_index}', tags=['REQUEST'])
async def get_info_by_index(item_index:int):
    try:
        return temp_database[item_index]
    except:
        HTTPException(status_code=202 , detail="index doesn't exist")
        
# Operation = Update
@app.put('/update/{item_index}', tags=["Update"])
async def UpdateItem(item_index:int , item: Contact ):
    try:
        temp_database[item_index]= item
        return item
    except:
        return HTTPException(status_code=505 , detail= "item doesn't exist")
    
# Operation = DELETE

@app.delete('/delete/{item_index}', tags=["Delete"])
async def DeleteItem( item_index:int):
    try:
        temp_database.pop(item_index) 
        return {"Item Deleted"}    
    except IndexError:
        raise HTTPException(status_code=404 ,detail="Item doesn't exist")
    

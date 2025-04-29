from typing import Optional
from fastapi import FastAPI

app = FastAPI(
    title="My First FastAPI Project",
    description="This is a simple API to greet users by name.",
    version="1.0.0"
)

# -------------------------------
# 🏠 Basic GET Routes
# -------------------------------

@app.get("/", tags=["Root"])
def read_root():
    """Return a basic greeting"""
    return {"message": "Hello World"}

@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int, q: Optional[str] = None):
    """
    Get item by ID and optional query.
    
    Parameters:
    - item_id: int — ID of the item
    - q: Optional query string
    """
    return {"item_id": item_id, "query": q}

@app.get("/name/{name}", tags=["Greetings"])
def greet(name: str):
    """Personalized welcome message"""
    return {"message": f"Hello {name}, welcome to my first API tutorial!"}

# -------------------------------
# ✨ Tagged GET Routes
# -------------------------------

@app.get("/hello/{name}", tags=["Greetings"])
def say_hello(name: str):
    """Return a greeting message"""
    return {"message": f"Hello, {name}!"}

@app.get("/goodbye/{name}", tags=["Farewells"])
def say_goodbye(name: str):
    """Return a farewell message"""
    return {"message": f"Goodbye, {name}!"}

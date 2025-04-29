# fastapi-tutorials

A collection of FastAPI practice projects and tutorials.

## FastAPI Practice Projects

This repository contains my FastAPI learning projects, including GET, POST, PUT, PATCH, DELETE, and CRUD operations.




| Directory     | Description                                          |
|---------------|------------------------------------------------------|
| `01 GET`      | Basic GET endpoint to retrieve data                  |
| `02 POST`     | Handling POST requests with request body             |
| `03 PUT`      | Full update of an existing resource using PUT        |
| `04 PATCH`    | Partial update of a resource using PATCH             |
| `05 DELETE`   | Deleting resources using DELETE method               |
| `06 CRUD`     | Simple CRUD operations with in-memory data           |


## How to Run

### Step 1: Install Dependencies

Make sure you have Python installed. Then install the required packages:




pip install fastapi uvicorn


🚀 Step 2: Run the Application
Use the following command to run your FastAPI app (make sure you're in the same directory as main.py):

bash
Copy
Edit
uvicorn main:app --reload
main is the name of your Python file (e.g., main.py, so just use main)

app is the FastAPI instance (e.g., app = FastAPI())

The --reload flag makes the server restart automatically on code changes (useful during development).

🌐 Step 3: Access API Documentation
After running the server, open your browser and go to:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
This opens Swagger UI, where you can test all your API methods like:



- `GET`: Retrieve data
- `POST`: Submit new data
- `PUT`: Full update
- `PATCH`: Partial update
- `DELETE`: Remove data

You can also use:

arduino
Copy
Edit
http://127.0.0.1:8000/redoc
to access the ReDoc documentation.

✅ Now you're all set to test your FastAPI application!












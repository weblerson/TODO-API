from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class TODO(BaseModel):
    status: str
    assignment: str

app = FastAPI()

assignments = []

@app.get('/assignments')
def view():
    return assignments

@app.post('/create')
def create(todo: TODO):
    try:
        assignments.append({"status": todo.status, "tarefa": todo.assignment})

        return {"status": "success"}

    except:
        
        return {"status": "error"}

@app.post('/change')
def change(id: int, status: str):
    try:
        assignments[id]["status"] = status

        return {"status": "success"}

    except:

        return {"status": "error"}

@app.post('/delete')
def delete(id: int):
    try:
        assignments.remove(assignments[id])

        return {"status": "success"}

    except:
        
        return {"status": "error"}
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

class Todo(BaseModel):
    name: str
    completed: bool


# Mock database
todos = {}

# Getting all the Todos
@app.get("/", response_model=List[Todo])
async def read_todos():
    return list(todos.values())


# Posting and updating the single todo
@app.post("/", response_model=Todo)
async def create_todo(todo: Todo):
    todo_id = str(len(todos) + 1)
    todos[todo_id] = todo
    return todo


# Getting a single todo
@app.get("/{todo_id}", response_model=Todo)
async def read_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found :(")
    return todo


# Updating the todo 
@app.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, updated_todo: Todo):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found :(")
    todos[todo_id] = updated_todo
    return updated_todo


# Removing todo from the list.
@app.delete("/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found :(")
    del todos[todo_id]
    return todo

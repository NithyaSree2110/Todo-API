from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Todo API",
    description="A simple CRUD API built with FastAPI and Python 3.12.",
    version="1.0.0"
    )

tasks = [
    {"id": 1, "title": "Buy groceries", "done": False},
    {"id": 2, "title": "Read a book", "done": True},
    {"id": 3, "title": "Clean the room", "done": False},
]

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks",
         summary="Get all tasks",
    description="Returns a list of all tasks.")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}",summary="Get a task",
    description="Returns a task by its ID.")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", status_code=201,summary="Create a task",
    description="Creates a new task with a unique ID.")
def create_task(task_data: TaskCreate):
    if not task_data.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    new_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = {
        "id": new_id,
        "title": task_data.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

# PUT /tasks/{id} -> update title/done
@app.put("/tasks/{task_id}",summary="Update a task",
    description="Updates an existing task.")
def update_task(task_id: int, task_data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if task_data.title is not None:
                if not task_data.title.strip():
                    raise HTTPException(status_code=400, detail="Title cannot be empty")
                task["title"] = task_data.title
            if task_data.done is not None:
                task["done"] = task_data.done
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

# DELETE /tasks/{id} -> delete task (returns 204 No Content)
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT,summary="Delete a task",
    description="Deletes a task by its ID.")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

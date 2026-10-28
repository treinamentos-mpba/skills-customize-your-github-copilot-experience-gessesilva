# Código inicial para a tarefa de API REST com FastAPI

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    completed: bool


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks: list[Task] = []
next_task_id = 1


@app.get("/health")
def health_check():
    # TODO: Retorne {"status": "ok"}.
    pass


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Retorne a lista de tarefas.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    # TODO: Crie uma tarefa com um ID único e completed=False.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Encontre e retorne a tarefa ou lance HTTPException com status 404.
    pass


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    # TODO: Atualize o status completed ou lance HTTPException com status 404.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Remova a tarefa ou lance HTTPException com status 404.
    pass

# Código inicial para persistir tarefas de uma API FastAPI com SQLite

import sqlite3
from contextlib import closing
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Persistent Task API")
DATABASE_PATH = Path(__file__).with_name("tasks.db")


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    completed: bool


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with closing(get_connection()) as connection:
        with connection:
            # TODO: Crie a tabela tasks com id, title e completed.
            pass


initialize_database()


def task_from_row(row):
    return Task(
        id=row["id"],
        title=row["title"],
        completed=bool(row["completed"]),
    )


def find_task(connection, task_id):
    return connection.execute(
        "SELECT id, title, completed FROM tasks WHERE id = ?",
        (task_id,),
    ).fetchone()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    with closing(get_connection()) as connection:
        with connection:
            # TODO: Consulte as tarefas ordenadas por ID e converta as linhas em Task.
            pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    with closing(get_connection()) as connection:
        with connection:
            # TODO: Insira a tarefa com SQL parametrizado e obtenha o ID criado.
            pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    with closing(get_connection()) as connection:
        # TODO: Use find_task; retorne 404 se não existir ou converta a linha em Task.
        pass


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    with closing(get_connection()) as connection:
        with connection:
            # TODO: Atualize completed com parâmetros e retorne a tarefa atualizada.
            pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    with closing(get_connection()) as connection:
        with connection:
            # TODO: Exclua a tarefa e retorne 404 se nenhum registro for afetado.
            pass

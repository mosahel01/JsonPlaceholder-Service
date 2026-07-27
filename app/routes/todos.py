from fastapi import APIRouter, HTTPException

from app.schemas.todo import Todo, TodoCreate
from app.schemas.user import User
from app.services.todo_service import (
    fetch_todo_by_id,
    fetch_todos,
    fetch_user_by_id,
    fetch_user_todos,

    create_todo_service,
)

router = APIRouter()
"""
APIRouter class, used to group *path operations*, for example to structure
an app in multiple files. It would then be included in the `FastAPI` app, or
in another APIRouter (ultimately included in the app).
"""


@router.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello, FastAPI!"}


@router.get("/todos", response_model=list[Todo], status_code=201)
def list_todos():
    return fetch_todos()


@router.get("/todos/{todo_id}", response_model=Todo)
def read_todo(todo_id: int):
    todo = fetch_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found.")
    return todo


@router.get("/users/{user_id}/todos", response_model=list[Todo])
def list_user_todos(user_id: int):
    return fetch_user_todos(user_id)


@router.get("/users/{user_id}", response_model=User)
def list_user(user_id: int):
    return fetch_user_by_id(user_id)


@router.post("/todos")
def create_todo(todo: TodoCreate):
    print(type(todo))
    return create_todo_service(todo)


# define HTTP endpoints (/todos, /todos/{id})
# calls service functions
# contains almost no business logic

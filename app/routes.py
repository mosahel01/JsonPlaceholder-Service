from fastapi import APIRouter, HTTPException

from app.services import get_all_todos, get_todo, get_user

router = APIRouter()


@router.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello, FastAPI!"}


@router.get("/todos")
def get_todos() -> list[dict]:
    return get_all_todos()


@router.get("/todos/{todo_id}")
def get_single_todo(todo_id: int):
    todo = get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found.")
    return todo


@router.get("/users/{user_id}/todos")
def get_user_by_id(user_id: int):
    return get_user(user_id)


# @router.get("/todos") means when
# someone visits GET/todos run the function below

# APIrouter is a class used to organise and group related API endpoints
# into modular, reusable components, facilitating scalable project structures.

# @router.get("/todos/{todo_id}")
# FastAPI automatically passes todo_id to get_single_todo(todo_id:int)

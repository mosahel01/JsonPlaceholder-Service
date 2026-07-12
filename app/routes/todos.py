from fastapi import APIRouter, HTTPException
from services.todo_services import get_all_todos, get_todo, get_user

app = APIRouter()


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello, FastAPI!"}


@app.get("/todos")
def get_todos():
    return get_all_todos()


@app.get("/todos/{todo_id}")
def get_single_todo(todo_id: int):
    todo = get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found.")
    return todo


@app.get("/users/{user_id}/todos")
def get_user_by_id(user_id: int):
    return get_user(user_id)

# define HTTP endpoints (/todos, /todos/{id})
# calls service functions
# contains almost no business logic

import requests

from app.config import BASE_URL, REQUEST_TIMEOUT


# GET Service
def fetch_service(endpoint: str):
    response = requests.get(f"{BASE_URL}{endpoint}", timeout=REQUEST_TIMEOUT)
    response.raise_for_status()  # avoids ignoring HTTP errors
    return response.json()


def fetch_todos(completed: bool | None = None):
    if completed is None:
        return fetch_service("/todos")
    return fetch_service(f"/todos?completed={str(completed).lower()}")


def fetch_todo_by_id(todo_id: int):
    return fetch_service(f"/todos/{todo_id}")


def fetch_user_todos(user_id: int):
    return fetch_service(f"/users/{user_id}/todos")


def fetch_user_by_id(user_id: int):
    return fetch_service(f"/users/{user_id}")


# # POST Service
# def create_service(endpoint: str):
#     response = requests.post(f"{BASE_URL}/todos", json={endpoint}.model_dump())
#     return response.json()

# def create_todo_service(todo: TodoCreate):
#     return create_service(todo)

def create_todo_service(todo: TodoCreate):
    response = requests.post(
        f"{BASE_URL}/todos", 
        json=todo.model_dump()
    )

    return response.json()


# business logic here
# talks to jsonplaceholder
# handles API requests
# returns python data to the routes

# since service layer is making requests
# it should handle HTTP errors with response.raise_for_status()
# it also sets timeouts if the server won't respond.

import requests

from app.config import BASE_URL, REQUEST_TIMEOUT


# GET service
def fetch_service(endpoint: str):
    response = requests.get(f"{BASE_URL}{endpoint}", timeout=REQUEST_TIMEOUT)
    response.raise_for_status()  # raise on http errors
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


# POST service
def create_todo_service(todo: TodoCreate):
    # requests converts the dict to json
    response = requests.post(
        f"{BASE_URL}/todos",
        json=todo.model_dump(),  # convert model to dict
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    # parse json response into python dict/list from requests.post()
    return response.json()

# service layer
# handles api requests
# returns python data
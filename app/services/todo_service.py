import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(endpoint: str):
    response = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
    return response.json()


def fetch_todos(completed: bool | None = None):
    if completed is None:
        return fetch_json("/todos")
    return fetch_json(f"/todos?completed={str(completed).lower()}")


def fetch_todo_by_id(todo_id: int):
    return fetch_json(f"/todos/{todo_id}")


def fetch_user_todos(user_id: int):
    return fetch_json(f"/users/{user_id}/todos")


# business logic here
# talks to jsonplaceholder
# handles API requests
# returns python data to the routes

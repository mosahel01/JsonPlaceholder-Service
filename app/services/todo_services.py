import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(endpoint: str):
    response = requests.get(f"{BASE_URL}{endpoint}")
    return response.json()


def get_all_todos(completed: bool | None = None):
    if completed is None:
        return fetch_json("/todos")
    return fetch_json(f"/todos?completed={str(completed).lower()}")


def get_todo(todo_id: int):
    return fetch_json(f"/todos/{todo_id}")


def get_user(user_id: int):
    return fetch_json(f"/users/{user_id}/todos")


# talks to jsonplaceholder
# handles API requests
# returns python data to the routes

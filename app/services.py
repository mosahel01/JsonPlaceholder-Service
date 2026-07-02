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


# requests let us make HTTP requests
# when we need todos, we'll call get_all_todos()
# requests.get(..) makes a GET request to this URL

# instead of immediately getting a list of dictionary,
# PYTHON stores the whole HTTP response inside `response`

# .json() converts the JSON response into Python Objects -> Lists
# false -> False, python converts JSON into native Python Objects

# *list[dict] type hint as returned response.json() would be list

# completed = query parameter
# todo_id = path parameters

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_all_todos(completed: bool | None = None) -> list[dict]:
    if completed is None:
        response = requests.get(f"{BASE_URL}/todos")
    else:
        response = requests.get(f"{BASE_URL}/todos/completed={str(completed).lower()}")
    return response.json()


# todo_id is passed from routes.py through routes
def get_todo(todo_id: int) -> list[dict]:
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    return response.json()


def get_user(user_id: int):
    response = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    return response.json()


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

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
def create_todo_service(todo: Todo):
    # requests converts the dict to json
    # response is the python object representing entire HTTP Response
    # status_code, headers, text, json() etc
    response = requests.post(
        f"{BASE_URL}/todos",
        json=todo.model_dump(),  # converts TodoCreate object to python dictionary
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    # Please take the JSON body from that HTTP response and convert it into python dict
    # FastAPI will convert this python dict into JSON later after
    # going through routes and pydantic.
    return response.json()  # extracts JSON out of Requests Response


# PUT service
def update_todo_service(todo_id: int, todo: TodoCreate):
    response = requests.put(
        f"{BASE_URL}/todos/{todo_id}",
        json=todo.model_dump(),
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def update_todo_service_partial(todo_id: int, todo: TodoUpdate):
    response = requests.patch(
        f"{BASE_URL}/todos/{todo_id}",
        json=todo.model_dump(),
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def delete_todo_service(todo_id: int):
    response = requests.delete(
        f"{BASE_URL}/todos/{todo_id}",
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()


# service layer
# handles api requests
# returns python data

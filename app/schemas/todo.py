from pydantic import BaseModel


class Todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool = False  # sets a default value if not provided during creation


class TodoCreate(BaseModel):
    userId: int
    title: str
    completed: bool


# No ID as server is responsible for creating IDs
# pydantic model = schema
# pydantic validates/filters outgoing data
# from routes before fastapi converts it to JSON

# Services -> Route -> [Pydantic] -> FastAPI -> Client

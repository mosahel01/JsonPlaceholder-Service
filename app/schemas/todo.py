from pydantic import BaseModel


class Todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


# pydantic model = schema
# pydantic validates outgoing data from routes
# before fastapi converts it to JSON

# Services -> Route -> [Pydantic] -> FastAPI -> Client

from fastapi import FastAPI

from app.routes.todos import router

app = FastAPI()  # creates fastapi app
app.include_router(router)  # includes all routers

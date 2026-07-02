from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# takes routes in routes.py and add them to this application
app.include_router(router)

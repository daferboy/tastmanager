from fastapi import FastAPI
from src.utils.database import Base, engine
from src.tasks.models import Task
from src.users.model import User
from src.tasks.router import task_routes
from src.users.router import user_routes

Base.metadata.create_all(engine)

app = FastAPI(
    title="Task Management App",
    description="Task management using APIs",
    version="1.0.0"
)

app.include_router(task_routes)
app.include_router(user_routes)

@app.get("/")
def home():
    return {
        "":f"Welcome to {app.title}",
        "Description":f"{app.description}",
        "Version":f"{app.version}"
    }

@app.get("/health")
def health():
    return{
        "status":"Ok"
    }
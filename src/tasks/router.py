from fastapi import APIRouter,Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.database import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/createtask")
def createtask(data:TaskSchema, db = Depends(get_db)):
    return controller.createtask(data, db)
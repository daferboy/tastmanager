from fastapi import APIRouter,Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.database import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/createtask")
def createtask(data:TaskSchema, db = Depends(get_db)):
    return controller.createtask(data, db)

@task_routes.get("/")
def get_tasks(db = Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/{task_id}")
def get_task(task_id:int, db = Depends(get_db)):
    return controller.get_task(task_id,db)

@task_routes.put("/updatetask/{task_id}")
def update_task(task_id:int, data:TaskSchema, db = Depends(get_db)):
    return controller.update_task(task_id = task_id, data=data, db=db)
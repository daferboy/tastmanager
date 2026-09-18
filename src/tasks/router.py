from fastapi import APIRouter,Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema,TaskResponseSchema
from src.utils.database import get_db
from typing import List
from sqlalchemy.orm import Session

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/createtask", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def createtask(data:TaskSchema, db:Session = Depends(get_db)):
    return controller.createtask(data, db)

@task_routes.get("/", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_tasks(db:Session = Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_task(task_id:int, db:Session = Depends(get_db)):
    return controller.get_task(task_id,db)

@task_routes.put("/updatetask/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task(task_id:int, data:TaskSchema, db:Session = Depends(get_db)):
    return controller.update_task(task_id = task_id, data=data, db=db)

@task_routes.delete("/delete/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int, db:Session = Depends(get_db)):
    return controller.delete_task(task_id = task_id, db = db)
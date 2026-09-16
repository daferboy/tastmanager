from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import Task
from fastapi import HTTPException

def createtask(data:TaskSchema, db:Session):
    record = data.model_dump()
    print(record)
    task = Task(
        title = record['title'],
        description = record['description'],
        isCompleted = record['isCompleted']
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return{
        "status":"OK",
        "record":task
    }

def get_tasks(db:Session):
    tasks = db.query(Task).all()
    #for task in tasks:
    #   print(task.title, task.description)

    return{
        "status":"All Tasks",
        "task":tasks
    }

def get_task(task_id:int, db:Session):
    task = db.query(Task).get(task_id)
    if not task:
        return HTTPException(404, f"Task not found at id {task_id}")
    return{
        "Status":f"Task found at id {task_id}",
        "task":task
    }

def update_task(task_id:int, db:Session, data:TaskSchema):
    task = db.query(Task).get(task_id)
    if not task:
        return HTTPException(404, f"Task not found at id {task_id}")

    task.title = data.title
    task.description = data.description
    task.isCompleted = data.isCompleted

    db.add(task)
    db.commit()
    db.refresh(task)

    return{
        "Status": "Task Updated",
        "Updated Task": task
    }

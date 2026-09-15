from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import Task

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

from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import Task
from src.users.model import User
from fastapi import HTTPException

def createtask(data:TaskSchema, db:Session,user:User):
    record = data.model_dump()
    # print(record)
    task = Task(
        title = record['title'],
        description = record['description'],
        isCompleted = record['isCompleted'],
        user_id = user.id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    # return{
    #     "status":"OK",
    #     "record":task
    # }
    return task

def get_tasks(db:Session,user:User):
    tasks = db.query(Task).filter(Task.user_id == user.id).all()
    #for task in tasks:
    #   print(task.title, task.description)
    
    # return{
    #     "status":"All Tasks",
    #     "task":tasks
    # }
    return tasks

def get_task(task_id:int, db:Session, user:User):

    if not user or not getattr(user,"id", None):
        raise HTTPException(status_code=401, detail="Unauthorized to view task")

    task = db.query(Task).get(task_id)

    if not task:
        return HTTPException(status_code=404, detail=f"Task not found at id {task_id}")

    if task.user_id != user.id:
        raise HTTPException(status_code=401, detail="Unauthorized to view task")
    
    # return{
    #     "Status":f"Task found at id {task_id}",
    #     "task":task
    # }
    return task

def update_task(task_id:int, db:Session, data:TaskSchema):
    task = db.query(Task).get(task_id)
    if not task:
        return HTTPException(404, f"Task not found at id {task_id}")

    # task.title = data.title
    # task.description = data.description
    # task.isCompleted = data.isCompleted
    data = data.model_dump()
    for field, value in data.items():
        setattr(task, field, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    # return{
    #     "Status": "Task Updated",
    #     "Updated Task": task
    # }
    return task

def delete_task(task_id:int, db:Session):
    task = db.query(Task).get(task_id)
    # print(task)
    if not task:
        return HTTPException(404, f"Task not found at id {task_id}")

    db.delete(task)
    db.commit()

    # return{
    #     "status":"Task Deleted",
    #     "deleted task":task
    # }
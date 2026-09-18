from pydantic import BaseModel

class TaskSchema(BaseModel):
    title:str
    description: str
    isCompleted: bool = False

class TaskResponseSchema(BaseModel):
    task_id:int
    title:str
    description:str
    isCompleted: bool
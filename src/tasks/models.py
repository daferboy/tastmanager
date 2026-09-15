from sqlalchemy import Column,Integer,String,Boolean, DateTime
from sqlalchemy.sql import func
from src.utils.database import Base

class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False
    )
    title = Column(
        String(50),
        nullable=False
    )
    description = Column(
        String(250),
        nullable=False
    )
    isCompleted = Column(
        Boolean,
        nullable=False,
        default=False
    )
    createdAt = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
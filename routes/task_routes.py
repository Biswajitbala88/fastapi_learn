from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.task import Task
from schemas.task_schema import TaskCreate, TaskResponse
from typing import List

router = APIRouter()


# get all tasks
@router.get("/all-tasks", response_model = List[TaskResponse])
def all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks


# create task
@router.post("/create-task", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description
    )
    print(new_task)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task
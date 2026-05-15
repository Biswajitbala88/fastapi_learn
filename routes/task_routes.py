from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.task import Task
from schemas.task_schema import TaskCreate, TaskResponse

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskOut
from app.models.task import Task, TaskStatus
from app.services.db_service import get_db
from app.services.queue import push_task
from app.services.task_service import get_task_by_id

router = APIRouter()

@router.post("/tasks", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(url=task.url, type=task.type, status=TaskStatus.PENDING)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    push_task(db_task.id)
    return db_task

@router.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

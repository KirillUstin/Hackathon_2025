from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskOut
from app.services.task_service import create_task, get_task_by_id
from app.services.db_service import get_db
from app.services.queue import push_task_to_queue

router = APIRouter()

@router.post("/tasks", response_model=TaskOut)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = create_task(db, target=task.host, task_type=task.type)
    push_task_to_queue(db_task.id)
    return db_task

@router.get("/tasks/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task_schema import TaskCreate, TaskRead
from app.services.task_service import TaskService
from app.core.config import get_db

router = APIRouter()

@router.post("/tasks", response_model=TaskRead)
def create_task(task_create: TaskCreate, db: Session = Depends(get_db)):
    """
    POST /api/tasks
    1. Принимает JSON с host и type
    2. Создаёт задачу через TaskService
    3. Возвращает созданную задачу с ID и статусом
    """
    try:
        task = TaskService.create_task(db, task_create)
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

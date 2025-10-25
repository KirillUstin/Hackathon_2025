from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus
from app.schemas.task_schema import TaskCreate

def create_task_in_db(db: Session, task_data: TaskCreate) -> Task:
    """
    Сохраняем новую задачу в PostgreSQL
    """
    task = Task(
        host=task_data.host,
        type=task_data.type,
        status=TaskStatus.PENDING
    )
    db.add(task)
    db.commit()  # фиксируем изменения в базе
    db.refresh(task)  # обновляем объект task с ID и датами
    return task

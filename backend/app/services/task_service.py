from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus
from app.models.result import Result

# ------------------------------
# Создание новой задачи
# ------------------------------
def create_task(db: Session, target: str, checks: list[str] = None, task_type: str = "full_check") -> Task:
    if checks is None:
        checks = ["http", "ping", "dns"]  # по умолчанию
    
    task = Task(
        target=target,
        type=task_type,
        checks=checks,
        status=TaskStatus.PENDING
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# ------------------------------
# Создание результата для конкретной проверки
# ------------------------------
def create_result(db: Session, task_id: int, check_type: str, result_data: dict) -> Result:
    # Подготовим JSON для хранения результатов
    import json
    message = json.dumps(result_data, ensure_ascii=False)

    result = Result(
        task_id=task_id,
        status=result_data.get("status", "error"),
        message=message
    )
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

# ------------------------------
# Получение всех задач
# ------------------------------
def get_all_tasks(db: Session) -> list[Task]:
    return db.query(Task).order_by(Task.id.desc()).all()

# ------------------------------
# Получение задачи по ID
# ------------------------------
def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()

# ------------------------------
# Обновление статуса задачи
# ------------------------------
def update_task_status(db: Session, task: Task, status: TaskStatus):
    task.status = status
    db.commit()
    db.refresh(task)
    return task

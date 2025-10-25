from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus
from app.models.result import Result
from app.schemas.task_schema import TaskCreate
from app.services.db_service import create_task_in_db
from app.services.queue import push_task_to_queue

class TaskService:
    """
    TaskService — это "мозг" работы с задачами.
    Он инкапсулирует всю логику: создание задачи, постановка в очередь, обновление статусов.
    """

    @staticmethod
    def create_task(db: Session, task_data: TaskCreate) -> Task:
        """
        Создаём новую задачу:
        1. Сохраняем в базу данных через db_service
        2. Добавляем задачу в очередь Redis для агентов
        """
        task = create_task_in_db(db=db, task_data=task_data)

        push_task_to_queue(task)

        return task

import json
import redis
from app.core.config import REDIS_HOST, REDIS_PORT, REDIS_DB
from app.models.task import Task

# Подключение к Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

def push_task_to_queue(task: Task):
    """
    Кладём задачу в Redis для агентов.
    Агент будет её брать и выполнять проверку.
    """
    task_data = {
        "id": task.id,
        "host": task.host,
        "type": task.type
    }
    r.lpush("task_queue", json.dumps(task_data))  # кладём в список Redis

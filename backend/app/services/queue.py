import json
import redis
from app.core.config import settings
from app.models.task import Task

r = redis.from_url(settings.REDIS_URL, decode_responses=True)

def push_task_to_queue(task: Task):
    task_data = {
        "task_id": task.id,
        "target": task.target,
        "type": task.type,
        "checks": task.checks.split(",") if task.checks else ["http", "ping", "dns"]
    }
    r.lpush("task_queue", json.dumps(task_data))

def pop_task():
    item = r.rpop("task_queue")
    if item:
        return json.loads(item)
    return None

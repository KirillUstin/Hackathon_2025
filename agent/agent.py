import time
import requests
from config import BACKEND_URL, AGENT_TOKEN, AGENT_NAME
from checkers import http_check, ping_check, dns_check
from utils.logger import get_logger

logger = get_logger("agent")
HEADERS = {"x_token": AGENT_TOKEN}

def register_agent():
    #Регистрируем агента на бекенде
    try:
        r = requests.post(f"{BACKEND_URL}/api/agents/register", headers=HEADERS, json={"name": AGENT_NAME})
        logger.info(f"Registered agent: {r.status_code} {r.text}")
    except Exception as e:
        logger.error(f"Registration failed: {e}")

def send_result(task_id: str, checker: str, result: dict):
    #Отправка результата проверки на бекенд
    try:
        r = requests.post(
            f"{BACKEND_URL}/api/tasks/{task_id}/results",
            headers=HEADERS,
            json={"checker": checker, "result": result}
        )
        logger.info(f"Sent result for task {task_id}, checker {checker}: {r.status_code}")
    except Exception as e:
        logger.error(f"Failed to send result: {e}")

def process_task(task: dict):
    #Обработка одной задачи
    task_id = task.get("task_id")
    target = task.get("target")
    checks = task.get("checks", [])

    logger.info(f"Processing task {task_id} for target {target} with checks {checks}")

    for check_type in checks:
        if check_type == "http":
            res = http_check.check_http(target)
        elif check_type == "ping":
            res = ping_check.check_ping(target)
        elif check_type == "dns":
            res = dns_check.check_dns(target)
        else:
            res = {"status": "error", "error": f"Unknown check type {check_type}"}
        send_result(task_id, check_type, res)

def get_task():
    #Запрос задачи у бекенда
    try:
        r = requests.post(f"{BACKEND_URL}/api/agents/get_task", headers=HEADERS)
        if r.status_code == 200:
            return r.json()
        else:
            logger.info(f"No task available: {r.status_code}")
    except Exception as e:
        logger.error(f"Failed to get task: {e}")

if __name__ == "__main__":
    register_agent()
    while True:
        task = get_task()
        if task and "task_id" in task:
            process_task(task)
        else:
            time.sleep(2)

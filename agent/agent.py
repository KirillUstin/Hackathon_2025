import time
import json
import requests
import redis
from checkers.http_check import http_check
from checkers.ping_check import ping_check
from checkers.dns_check import dns_check
from utils.logger import get_logger
from config import REDIS_HOST, REDIS_PORT, REDIS_DB, BACKEND_URL, AGENT_NAME, AGENT_REGION


logger = get_logger()

# Подключение к Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

# Регистрация агента
def register_agent():
    data = {
        "name": AGENT_NAME,
        "ip_address": "127.0.0.1",  # Можно динамически определять
        "region": AGENT_REGION
    }
    response = requests.post(f"{BACKEND_URL}/api/agents", json=data)
    if response.status_code == 200:
        agent_id = response.json()["id"]
        logger.info(f"Agent registered with ID {agent_id}")
        return agent_id
    else:
        logger.error(f"Failed to register agent: {response.text}")
        return None

# Отправка heartbeat
def send_heartbeat(agent_id):
    try:
        response = requests.put(f"{BACKEND_URL}/api/agents/{agent_id}/heartbeat")
        if response.status_code == 200:
            logger.info("Heartbeat sent successfully")
        else:
            logger.warning(f"Heartbeat failed: {response.text}")
    except Exception as e:
        logger.error(f"Error sending heartbeat: {e}")

# Выполнение задачи
def execute_task(task_data):
    host = task_data["host"]
    check_type = task_data["type"]
    result = {"success": False, "output": None}

    try:
        if check_type == "http":
            result["success"], result["output"] = http_check(host)
        elif check_type == "ping":
            result["success"], result["output"] = ping_check(host)
        elif check_type == "dns":
            result["success"], result["output"] = dns_check(host)
        else:
            result["output"] = f"Unknown check type: {check_type}"
    except Exception as e:
        result["output"] = str(e)
    
    return result

# Основной цикл агента
def main():
    agent_id = register_agent()
    if not agent_id:
        logger.error("Agent registration failed, exiting")
        return

    while True:
        # 1. Отправляем heartbeat каждые 30 секунд
        send_heartbeat(agent_id)

        # 2. Получаем задачу из Redis (очередь task_queue)
        task_json = r.brpop("task_queue", timeout=5)  # brpop блокирует на 5 сек
        if task_json:
            _, task_str = task_json
            task_data = json.loads(task_str)
            logger.info(f"Received task: {task_data}")

            # 3. Выполняем задачу
            result = execute_task(task_data)

            # 4. Отправляем результат на backend
            response = requests.post(f"{BACKEND_URL}/api/results", json={
                "task_id": task_data["id"],
                "success": result["success"],
                "output": result["output"]
            })
            if response.status_code == 200:
                logger.info(f"Result sent for task {task_data['id']}")
            else:
                logger.error(f"Failed to send result: {response.text}")

        # Пауза между итерациями
        time.sleep(1)

if __name__ == "__main__":
    main()

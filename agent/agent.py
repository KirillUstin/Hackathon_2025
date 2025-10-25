import time
import requests
from config import BACKEND_URL, AGENT_TOKEN

HEADERS = {"x_token": AGENT_TOKEN}

while True:
    try:
        r = requests.post(f"{BACKEND_URL}/api/agents/get_task", headers=HEADERS)
        data = r.json()
        task_id = data.get("task_id")
        if task_id:
            print(f"Got task {task_id}, processing...")
            # Тут будет логика проверки (http, ping, dns)
            # ⚠️ Для MVP просто имитация
            time.sleep(2)
            print(f"Task {task_id} done")
        else:
            time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)

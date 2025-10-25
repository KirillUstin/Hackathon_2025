import os

# Отедактировать под свои значения, если будем использовать локальный Redis или другой URL
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")  # Если будет через Docker, указать имя сервиса
AGENT_TOKEN = os.getenv("AGENT_TOKEN", "supersecret")  # Заменить на реальный токен
AGENT_NAME = os.getenv("AGENT_NAME", "agent1")         # Уникальное имя агента

# agent/config.py
import os

AGENT_TOKEN = os.getenv("AGENT_TOKEN", "supersecret")
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")  # ⚠️ имя сервиса backend в docker-compose

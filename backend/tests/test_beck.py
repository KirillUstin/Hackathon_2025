# tests/test_agents.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)

def test_heartbeat_valid_token():
    headers = {"x_token": settings.AGENT_TOKEN}
    response = client.post("/api/agents/heartbeat", headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "alive"

def test_heartbeat_invalid_token():
    headers = {"x_token": "wrongtoken"}
    response = client.post("/api/agents/heartbeat", headers=headers)
    assert response.status_code == 403

def test_get_task_no_tasks():
    headers = {"x_token": settings.AGENT_TOKEN}
    response = client.post("/api/agents/get_task", headers=headers)
    assert response.status_code == 200
    assert response.json()["task"] is None

"""
Тесты для эндпоинтов, связанных с результатами (results).
Проверяются:
 - добавление результата;
 - получение результатов по ID задачи.
"""

from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


@pytest.fixture
def sample_task():
    """
    Создаёт тестовую задачу, чтобы у неё можно было добавить результат.
    """
    payload = {"target": "ya.ru", "checks": ["dns"]}
    resp = client.post("/api/tasks", json=payload)
    return resp.json()["id"]


def test_add_result(sample_task):
    """
    Проверяем добавление результата проверки (POST /api/results).
    """
    payload = {
        "task_id": sample_task,
        "checker": "dns",
        "result": {"status": "ok", "ip": "77.88.55.66"}
    }

    response = client.post("/api/results", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["task_id"] == sample_task
    assert data["checker"] == "dns"
    assert "created_at" in data


def test_get_results_by_task(sample_task):
    """
    Проверяем, что по ID задачи можно получить её результаты.
    """
    # Добавляем один результат
    payload = {
        "task_id": sample_task,
        "checker": "ping",
        "result": {"status": "reachable", "rtt_ms": 24}
    }
    client.post("/api/results", json=payload)

    # Запрашиваем результаты этой задачи
    response = client.get(f"/api/results/{sample_task}")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "checker" in data[0]
        assert "result" in data[0]

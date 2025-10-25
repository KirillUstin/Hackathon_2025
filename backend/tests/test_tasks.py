"""
Тесты для эндпоинтов, связанных с задачами (tasks).
Проверяются:
 - создание задачи;
 - получение задачи по ID;
 - получение списка задач;
"""

from fastapi.testclient import TestClient
from app.main import app  # основной объект FastAPI
import pytest

# создаём клиент, который будет посылать HTTP-запросы к нашему приложению
client = TestClient(app)


def test_create_task():
    """
    Проверяем, что можно создать задачу через POST /api/tasks
    и что в ответе приходят нужные поля.
    """
    payload = {
        "target": "example.com",
        "checks": ["ping", "http"]
    }

    response = client.post("/api/tasks", json=payload)

    # 1. Проверяем, что сервер ответил 200 OK
    assert response.status_code == 200

    # 2. Проверяем, что в ответе действительно есть данные задачи
    data = response.json()
    assert "id" in data
    assert data["target"] == "example.com"
    assert data["status"] in ("pending", "created")

    # 3. Возвращаем id для последующих тестов
    return data["id"]


def test_get_task_by_id():
    """
    Проверяем получение конкретной задачи по ID.
    Для этого сначала создаём задачу, потом запрашиваем её.
    """
    new_task = {"target": "8.8.8.8", "checks": ["ping"]}
    create_resp = client.post("/api/tasks", json=new_task)
    task_id = create_resp.json()["id"]

    # теперь запрашиваем задачу
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == task_id
    assert data["target"] == "8.8.8.8"


def test_list_tasks():
    """
    Проверяем, что /api/tasks возвращает список всех задач.
    """
    response = client.get("/api/tasks")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    # если хотя бы одна задача есть — у неё должны быть id и target
    if data:
        assert "id" in data[0]
        assert "target" in data[0]

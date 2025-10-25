# tests/test_tasks.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.services.db_service import SessionLocal, engine
from app.models.task import Base

# ⚠️ Создание тестовой БД в памяти для dry-run
@pytest.fixture(scope="module")
def test_db():
    # создаём таблицы
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_create_task(test_db):
    response = client.post("/api/tasks", json={"url": "http://example.com", "type": "http"})
    assert response.status_code == 200
    data = response.json()
    assert data["url"] == "http://example.com"
    assert data["type"] == "http"
    assert data["status"] == "PENDING"

def test_get_task(test_db):
    # создаём задачу через API
    response = client.post("/api/tasks", json={"url": "http://example.org", "type": "ping"})
    task_id = response.json()["id"]
    
    # получаем задачу
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["url"] == "http://example.org"

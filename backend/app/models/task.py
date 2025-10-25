from sqlalchemy import Column, Integer, String, Enum
from app.models.base import Base  # ✅ импортируем отсюда

import enum

# Определяем статус задачи (enum)
class TaskStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

# Основная таблица Task
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    target = Column(String(255), nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)

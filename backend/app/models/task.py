from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from app.core.config import Base  # SQLAlchemy Base импортируем из core/config

# Определяем возможные статусы задачи
class TaskStatus(PyEnum):
    PENDING = "pending"         # Задача создана, но не обработана
    IN_PROGRESS = "in_progress" # Агент начал проверку
    DONE = "done"               # Проверка завершена успешно
    FAILED = "failed"           # Проверка завершилась с ошибкой

class Task(Base):
    __tablename__ = "tasks"  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор задачи
    host = Column(String, nullable=False)               # Домен или IP, который проверяем
    type = Column(String, nullable=False)               # Тип проверки: http, ping, dns, tcp
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)  # Статус задачи
    created_at = Column(DateTime, default=datetime.utcnow)          # Дата создания
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Дата последнего обновления

    # Связь с таблицей результатов (одна задача → несколько результатов, например при нескольких типах проверок)
    results = relationship("Result", back_populates="task", cascade="all, delete-orphan")

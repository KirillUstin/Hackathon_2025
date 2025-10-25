from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.config import Base

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)        # Уникальный идентификатор результата
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)  # Ссылка на задачу
    success = Column(Boolean, default=False)                  # Статус успешности проверки
    output = Column(Text, nullable=True)                      # Результат проверки (например, ответ сервера, время, ошибки)
    checked_at = Column(DateTime, default=datetime.utcnow)    # Когда была выполнена проверка

    # Связь с задачей
    task = relationship("Task", back_populates="results")

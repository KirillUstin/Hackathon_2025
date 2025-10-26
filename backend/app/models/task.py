from sqlalchemy import Column, Integer, String, Enum
from app.models.base import Base
import enum

class TaskStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)           # тип задачи, например "check"
    target = Column(String(255), nullable=False)       # хост или домен
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    checks = Column(String(255), default="http,ping,dns")  # через запятую
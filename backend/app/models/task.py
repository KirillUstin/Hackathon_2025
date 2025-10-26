from sqlalchemy import Column, Integer, String, Enum, JSON
from sqlalchemy.orm import relationship
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
    type = Column(String(50), nullable=False)         
    target = Column(String(255), nullable=False)      # что проверять (домен, IP)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    checks = Column(JSON, default=[])                 #список проверок ["http", "ping", "dns", "tcp", "traceroute"]

    results = relationship("Result", back_populates="task")

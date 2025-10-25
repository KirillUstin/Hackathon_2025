from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.config import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)           # Уникальный ID агента
    name = Column(String, nullable=False)                        # Имя агента
    ip_address = Column(String, nullable=False)                  # IP агента
    region = Column(String, nullable=True)                       # Регион, например RU, US
    is_active = Column(Boolean, default=True)                    # Живой или нет
    last_heartbeat = Column(DateTime, default=datetime.utcnow)   # Время последнего heartbeat
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Можно добавить связь с задачами, если захотим хранить историю
    # tasks = relationship("Task", back_populates="agent")

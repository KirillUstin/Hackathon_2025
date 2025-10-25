from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class TaskStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    type = Column(String, nullable=False)  # http, ping, dns
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    results = relationship("Result", back_populates="task")

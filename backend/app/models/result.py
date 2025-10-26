from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from .task import Base

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    check_type = Column(String, nullable=False)   #тип проверки (http, ping, dns, tcp, traceroute)
    result = Column(JSONB, nullable=False)       #JSON с результатом

    task = relationship("Task", back_populates="results")

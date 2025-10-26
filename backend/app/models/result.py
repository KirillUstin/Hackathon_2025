from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from sqlalchemy.dialects.postgresql import JSONB

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    check_type = Column(String(50), nullable=False)       # тип проверки: http, ping, dns, tcp, traceroute
    status = Column(String(50), nullable=False)          # success, failed
    message = Column(String, nullable=True)              # краткое описание
    details = Column(JSONB, nullable=True)               # детальные данные в формате JSON (например, traceroute hops)

    task = relationship("Task", back_populates="results")

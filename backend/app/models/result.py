from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .task import Base

class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    status = Column(String)
    message = Column(String, nullable=True)

    task = relationship("Task", back_populates="results")

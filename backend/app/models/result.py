from sqlalchemy import Column, String, JSON, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from backend.app.core.db import Base

class Result(Base):
    __tablename__ = "results"
    id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"), primary_key=True)
    checker = Column(String, nullable=False)
    result = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())


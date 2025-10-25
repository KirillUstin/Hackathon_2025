from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
import datetime
import uuid

Base = declarative_base()

def gen_uuid():
    return str(uuid.uuid4())

class Task(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True, default=gen_uuid)
    target = Column(Text, nullable=False)
    checks = Column(JSON, nullable=False)  #["http","ping","dns"]
    status = Column(String(32), nullable=False, default="pending")
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

class Result(Base):
    __tablename__ = "results"
    # Для простоты id будет уникальным UUID
    id = Column(String, primary_key=True, default=gen_uuid)
    task_id = Column(String, nullable=False)
    checker = Column(String(32), nullable=False)
    result = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)

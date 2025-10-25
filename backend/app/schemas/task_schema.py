from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Статусы задачи для сериализации
class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    FAILED = "failed"

# Схема для создания новой задачи (входные данные)
class TaskCreate(BaseModel):
    host: str = Field(..., example="example.com")  # Домейн/IP
    type: str = Field(..., example="http")         # Тип проверки

# Схема для результата проверки
class ResultRead(BaseModel):
    id: int
    success: bool
    output: Optional[str]
    checked_at: datetime

    class Config:
        orm_mode = True  # Чтобы SQLAlchemy-модели могли автоматически конвертироваться в Pydantic

# Схема для чтения задачи вместе с результатами
class TaskRead(BaseModel):
    id: int
    host: str
    type: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime
    results: List[ResultRead] = []

    class Config:
        orm_mode = True

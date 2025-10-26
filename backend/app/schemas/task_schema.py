from pydantic import BaseModel
from typing import List, Optional

class TaskResult(BaseModel):
    status: str
    message: Optional[str]

class TaskCreate(BaseModel):
    host: str
    type: str = "full_check"

class TaskOut(BaseModel):
    id: int
    target: str
    type: str
    status: str

    class Config:
        orm_mode = True  # чтобы можно было возвращать SQLAlchemy объекты


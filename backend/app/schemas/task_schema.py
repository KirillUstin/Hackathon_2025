from pydantic import BaseModel
from typing import List, Optional

class TaskCreate(BaseModel):
    url: str
    type: str  # http, ping, dns

class TaskResult(BaseModel):
    status: str
    message: Optional[str]

class TaskOut(BaseModel):
    id: int
    url: str
    type: str
    status: str
    results: List[TaskResult] = []

    class Config:
        orm_mode = True

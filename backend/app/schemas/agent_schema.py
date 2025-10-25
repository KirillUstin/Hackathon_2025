from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Для регистрации агента
class AgentCreate(BaseModel):
    name: str
    ip_address: str
    region: Optional[str] = None

# Для чтения данных агента
class AgentRead(BaseModel):
    id: int
    name: str
    ip_address: str
    region: Optional[str] = None
    is_active: bool
    last_heartbeat: datetime

    class Config:
        orm_mode = True

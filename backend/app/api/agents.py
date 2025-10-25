from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.agent_schema import AgentCreate, AgentRead
from app.services.agent_service import register_agent, update_heartbeat
from app.core.config import get_db

router = APIRouter()

# Регистрация нового агента
@router.post("/agents", response_model=AgentRead)
def create_agent(agent_create: AgentCreate, db: Session = Depends(get_db)):
    """
    Агент присылает свои данные: name, ip_address, region
    Backend сохраняет его в базе
    """
    agent = register_agent(db, agent_create)
    return agent

# Heartbeat агента
@router.put("/agents/{agent_id}/heartbeat", response_model=AgentRead)
def heartbeat(agent_id: int, db: Session = Depends(get_db)):
    """
    Агент присылает heartbeat, чтобы сказать, что он живой
    """
    agent = update_heartbeat(db, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

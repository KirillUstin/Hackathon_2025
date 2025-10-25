from sqlalchemy.orm import Session
from app.models.agent import Agent
from app.schemas.agent_schema import AgentCreate
from datetime import datetime

def register_agent(db: Session, agent_data: AgentCreate) -> Agent:
    """
    Создаём нового агента в базе данных
    """
    agent = Agent(
        name=agent_data.name,
        ip_address=agent_data.ip_address,
        region=agent_data.region
    )
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def update_heartbeat(db: Session, agent_id: int) -> Agent:
    """
    Обновляем поле last_heartbeat, чтобы отметить агента как живого
    """
    agent = db.query(Agent).filter(Agent.id == agent_id).first()
    if agent:
        agent.last_heartbeat = datetime.utcnow()
        agent.is_active = True
        db.commit()
        db.refresh(agent)
    return agent

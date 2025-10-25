from fastapi import APIRouter, Header, HTTPException, Depends
from app.core.config import settings
from app.services.queue import pop_task
from sqlalchemy.orm import Session
from app.services.db_service import get_db

router = APIRouter()

def verify_token(x_token: str = Header(...)):
    if x_token != settings.AGENT_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return True

@router.post("/agents/heartbeat")
def heartbeat(auth: bool = Depends(verify_token)):
    return {"status": "alive"}

@router.post("/agents/get_task")
def get_task(auth: bool = Depends(verify_token), db: Session = Depends(get_db)):
    task_id = pop_task()
    if not task_id:
        return {"task": None}
    return {"task_id": task_id}

@router.post("/agents/report")
def report(task_id: int, status: str, message: str = None, auth: bool = Depends(verify_token), db: Session = Depends(get_db)):
    """Агент отправляет результаты проверки"""
    from app.services.task_service import create_result
    result = create_result(db, task_id, status, message)
    return {"result_id": result.id}

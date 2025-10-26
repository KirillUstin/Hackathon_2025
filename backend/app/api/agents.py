from fastapi import APIRouter, Header, HTTPException, Depends
from app.core.config import settings
from app.services.queue import pop_task
from sqlalchemy.orm import Session
from app.services.db_service import get_db

router = APIRouter()

# Проверка токена агента
def verify_token(x_token: str = Header(...)):
    if x_token != settings.AGENT_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")
    return True

# Эндпоинт heartbeat
@router.post("/agents/heartbeat")
def heartbeat(auth: bool = Depends(verify_token)):
    return {"status": "alive"}

# Эндпоинт получения задачи
@router.post("/agents/get_task")
def get_task(auth: bool = Depends(verify_token), db: Session = Depends(get_db)):
    task = pop_task()
    if not task:
        return {"task": None}
    return {"task_id": task.id, "target": task.target, "checks": task.checks}  # ⚠️ важно вернуть список проверок

# Эндпоинт отправки результата
@router.post("/agents/report")
def report(task_id: int, check_type: str, result: dict, auth: bool = Depends(verify_token), db: Session = Depends(get_db)):
    """
    Агент отправляет результат одной проверки (http, ping, dns, tcp, traceroute)
    result: dict с результатом
    """
    from app.services.task_service import create_result
    res = create_result(db, task_id, check_type, result)
    return {"result_id": res.id}

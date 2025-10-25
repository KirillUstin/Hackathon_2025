from fastapi import APIRouter
router = APIRouter()

@router.post("/")
async def create_task(payload: dict):
    return {"task_id": "uuid-example", "status": "pending"}

@router.get("/{task_id}")
async def get_task(task_id: str):
    return {"task_id": task_id, "status": "pending", "results": []}


from fastapi import FastAPI
from app.api import tasks, agents

app = FastAPI(title="Aeza Checker Backend")

app.include_router(tasks.router, prefix="/api")
app.include_router(agents.router, prefix="/api")

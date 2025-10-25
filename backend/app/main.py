from fastapi import FastAPI
from app.api import tasks

app = FastAPI(title="Aeza Checker MVP")
app.include_router(tasks.router, prefix="/api/tasks")


from fastapi import FastAPI
from app.api import tasks, agents
from app.core.config import Base, engine

# Создаём все таблицы (если ещё не созданы)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Aeza Checker API", version="0.1.0")

# Роутеры API
app.include_router(tasks.router, prefix="/api", tags=["Tasks"])
app.include_router(agents.router, prefix="/api", tags=["Agents"])

@app.get("/")
def root():
    return {"message": "Aeza Checker API is running"}

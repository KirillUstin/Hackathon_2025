from fastapi import FastAPI
from app.api import tasks, agents
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Aeza Checker Backend")

app.include_router(tasks.router, prefix="/api")
app.include_router(agents.router, prefix="/api")


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL фронта
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


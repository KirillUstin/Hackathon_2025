# backend/app/core/config.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # ⚠️ В Docker эти значения будут переопределяться через env
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "aeza"
    POSTGRES_HOST: str = "db"         # имя сервиса PostgreSQL в docker-compose
    POSTGRES_PORT: int = 5432

    REDIS_URL: str = "redis://redis:6379/0"  # имя сервиса Redis в docker-compose

    AGENT_TOKEN: str = "supersecret"  # токен для агентов

    class Config:
        env_file = ".env"  # ⚠️ при выгрузке на GitHub можно оставить env.example

settings = Settings()

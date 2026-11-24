import logging
import os

import psycopg
from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI(
    title="PCPulse",
    description="Приложение для мониторинга и апгрейда ПК",
    version="0.2.0",
)

TEAM_NAME = "PCPulse"

logger = logging.getLogger("uvicorn.error")


@app.get("/")
async def root():
    """Корневой эндпоинт."""
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    """Проверка приложения и подключения к базе данных."""
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "database": "DATABASE_URL is not set",
            },
        )

    try:
        with psycopg.connect(database_url, connect_timeout=3) as connection:
            connection.execute("SELECT 1")
    except psycopg.Error as error:
        logger.warning("Health check: database is unavailable: %s", error)
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "database": "unavailable",
            },
        )

    return {"status": "healthy", "database": "ok"}


@app.get("/version")
async def version():
    """Версия приложения и команда-владелец."""
    return {"version": app.version, "team": TEAM_NAME}

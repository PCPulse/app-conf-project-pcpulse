from fastapi import FastAPI


app = FastAPI(
    title="PCPulse",
    description="Приложение для мониторинга и апгрейда ПК",
    version="0.2.0",
)

TEAM_NAME = "PCPulse"


@app.get("/")
async def root():
    """Корневой эндпоинт."""
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    """Проверка работоспособности приложения."""
    return {"status": "healthy"}


@app.get("/version")
async def version():
    """Версия приложения и команда-владелец."""
    return {"version": app.version, "team": TEAM_NAME}
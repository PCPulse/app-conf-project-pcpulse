# Схема окружения проекта

Команда: PCPulse.

Проект: приложение для мониторинга и апгрейда ПК.

## Таблица сервисов

| Сервис | Образ или сборка | Порты `хост:контейнер` | Переменные окружения (только имена) | Тома | Зависит от (условие) | Healthcheck |
|---|---|---|---|---|---|---|
| app | build: .; базовый образ python:3.13-slim | ${APP_PORT:-8000}:8000 — обращения браузера и curl к API | DATABASE_URL | Нет | db: service_healthy | GET /health проверяет подключение к базе |
| db | postgres:16 | На хост не публикуются; внутри сети — 5432 | POSTGRES_PASSWORD, POSTGRES_DB | pgdata:/var/lib/postgresql/data | Нет | pg_isready -h localhost -U postgres -d app |

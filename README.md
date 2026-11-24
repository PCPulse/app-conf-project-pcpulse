<img src="./images/pcpulse_logo.png" alt="Taskflow logo" width="900">


# PCPulse

Приложение для мониторинга производительности ПК с игровым оверлеем и рекомендациями по апгрейду. Собирает показатели процессора, видеокарты и оперативной памяти, сохраняет статистику и анализирует её по заданным правилам. Получает системные требования игр через RAWG API и сравнивает их с характеристиками ПК. Результаты анализа помогают пользователю разобраться в возможных причинах снижения производительности и подобрать совместимые комплектующие.

## Команда

- **Чувильчиков Кирилл** — Team Lead / Аналитик.
- **Судец-Ребров Арсений** — Frontend / UI/UX.
- **Редков Максим** — Backend Developer.
- **Булавин Данила** — Desktop Developer.

## Стек технологий

### Backend

- Python 3.13 для окружения практики.
- FastAPI.
- Uvicorn.
- Pydantic.
- HTTPX.
- PostgreSQL 16 для окружения практики.

### Desktop

- C# + .NET.
- WPF + XAML.
- MVVM.
- HttpClient.

### Мониторинг и оверлей

- LibreHardwareMonitorLib.
- Windows Performance Counters.
- WPF + Win32 API.

### Внешний API

- RAWG API — информация об играх и системные требования.

## Архитектура

```text
Desktop (WPF) ──▶ Backend API (FastAPI) ──▶ RAWG API
      │                    │              (требования игр)
      ▼                    ▼
Мониторинг ПК       Анализ и подбор
(LibreHardware     по заданным правилам
 MonitorLib)               │
                           ▼
                       PostgreSQL 16
                  (история показателей,
                   каталог комплектующих)
```

## Статус

Проект в разработке.

## Запуск через Docker Compose

Нужно: запущенный Docker с Compose v2 или новее. Для локальной разработки используется Python 3.13.

Скачать проект:

```powershell
git clone https://github.com/PCPulse/app-conf-project-pcpulse.git
cd app-conf-project-pcpulse
```

Если репозиторий уже скачан, повторно клонировать его не нужно.

1. Создать файл переменных:

   ```powershell
   Copy-Item .env.example .env
   ```

   Git Bash, Linux и macOS:

   ```bash
   cp .env.example .env
   ```

2. В `.env` заменить `changeme` своим паролем базы: латинские буквы и цифры.

3. Запустить стек:

   ```powershell
   docker compose up --build
   ```

4. Во втором терминале проверить:

   ```powershell
   curl.exe -i http://localhost:8000/health
   ```

   В Git Bash, Linux и macOS: `curl -i http://localhost:8000/health`.

После готовности приложения ожидается HTTP 200:

```json
{"status":"healthy","database":"ok"}
```

Документация: http://localhost:8000/docs

Если порт 8000 занят, установить в `.env` `APP_PORT=8001` и обращаться к http://localhost:8001/health.

Остановка: Ctrl+C или `docker compose down`.

Удаление вместе с данными базы: `docker compose down -v`.

## Локальная разработка без Docker

Требуется установленный uv.

```powershell
uv sync --locked
uv run uvicorn main:app --reload
```

Без DATABASE_URL эндпоинт `/health` возвращает HTTP 503:

```json
{"status":"unhealthy","database":"DATABASE_URL is not set"}
```

Эндпоинт `/` продолжает возвращать HTTP 200.

## API

### GET /version

Возвращает версию приложения и название команды.

Запрос к запущенному приложению:

```powershell
curl.exe -i http://127.0.0.1:8000/version
```

Ответ: HTTP 200.

```json
{"version":"0.2.0","team":"PCPulse"}
```

### GET /health

Проверяет подключение к PostgreSQL.

При доступной базе возвращает HTTP 200 и `{"status":"healthy","database":"ok"}`.

При отсутствии DATABASE_URL или недоступности базы возвращает HTTP 503.

## Лицензия

MIT.

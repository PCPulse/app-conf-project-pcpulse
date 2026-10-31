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

- Python 3.11+.
- FastAPI.
- Uvicorn.
- Pydantic.
- HTTPX.
- SQLite.

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
                         SQLite
                  (история показателей,
                   каталог комплектующих)
```

## Статус

Проект в разработке.

## Установка и запуск

Для запуска текущего Backend API нужен Python 3.11+. Выполните команды из корня репозитория:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

После запуска доступны:

- Документация API: http://127.0.0.1:8000/docs.
- Проверка работоспособности: http://127.0.0.1:8000/health — ответ `{"status":"healthy"}`.

Параметр `--reload` предназначен для локальной разработки.

## Лицензия

MIT.

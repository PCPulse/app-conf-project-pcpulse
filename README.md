<img src="./images/pcpulse_logo.png" alt="Taskflow logo" width="900">


# PCPulse

Приложение для мониторинга производительности ПК с игровым оверлеем и рекомендациями по апгрейду. Собирает показатели процессора, видеокарты и оперативной памяти, сохраняет статистику и использует машинное обучение для выявления необычного поведения оборудования. Результаты анализа помогают пользователю разобраться в возможных причинах снижения производительности.

## Команда

- **Чувильчиков К.М.** — Team Lead.
- **Судец-Ребров А.В.** — Backend Developer / Tech Lead.
- **Редков М.А.** — Desktop Developer.

## Стек технологий

### Backend

- Python 3.11+.
- FastAPI.
- Uvicorn.
- Pydantic.
- SQLite.

### ML / аналитика

- Python 3.11+.
- scikit-learn — Isolation Forest.
- pandas.
- NumPy.
- joblib.

### Desktop

- C# + .NET.
- WPF + XAML.
- MVVM.
- HttpClient.

### Мониторинг и оверлей

- LibreHardwareMonitorLib.
- Windows Performance Counters.
- WPF + Win32 API.

## Архитектура

```text
Desktop (WPF) ──▶ Backend API (FastAPI) ──▶ ML (scikit-learn)
                         │                       │
                         ▼                       ▼
                       SQLite                Model Store
                                         (моделей в Git нет)
```

## Статус

Проект в разработке.

## Установка и запуск

(Будет добавлено позже) 

## Лицензия

MIT.

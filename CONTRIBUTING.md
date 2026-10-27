# Правила работы в команде

## Git-стратегия

Мы используем GitHub Flow.

Рабочая ветка создаётся от актуальной main. Изменения возвращаются в main через Pull Request после approval другого участника команды.

```text
main -> рабочая ветка -> Pull Request -> approval -> main
```

### Ветвление

Формат имени: префикс/краткое-описание.

Описание пишется латиницей, слова разделяются дефисами.

Префиксы:

- feature/ — новые функции;
- bugfix/ — исправление багов;
- docs/ — документация;
- chore/ — зависимости и служебные изменения.

Примеры:

- feature/version-endpoint;
- bugfix/health-response;
- docs/contributing-rules;
- chore/dependency-files.

### Коммиты

Используем Conventional Commits.

Формат: тип: описание изменения.

- feat: новая функция;
- fix: исправление бага;
- docs: изменения документации;
- style: форматирование кода;
- refactor: рефакторинг;
- test: добавление тестов;
- chore: рутинные задачи.

Примеры из истории репозитория:

- feat: add initial FastAPI application with health check
- fix: correct indentation in FastAPI application

## Code Review

### Регламент code review

- Ревьюер назначается автором PR при создании, из числа участников команды.
- Автор PR не может одобрить собственный PR — approval всегда ставит другой участник.
- Срок первого ответа ревьюера: 24 часа с момента создания PR.
- Автор отвечает на каждый комментарий: правкой либо аргументом, почему правка не нужна.
- Комментарий сокомандника закрывает (Resolve) тот, кто его оставил.
- Комментарий ревьюера другой команды закрывает автор PR после ответа ревьюера в том же обсуждении («исправлено, принимаю») или его Approve.
- Два круга Request changes без сближения позиций — вопрос выносится на встречу команды.

### Критерии approval

Ревьюер ставит Approve, только если выполнено всё:

1. Чек-лист автора в PR заполнен полностью.
2. Ветка названа по шаблону из раздела «Ветвление».
3. Все коммиты в PR начинаются с типа Conventional Commits.
4. В diff нет .env, ключей, паролей, токенов.
5. Локальный запуск по инструкции из раздела «Как проверить» даёт описанный результат.
6. Все комментарии предыдущих кругов ревью отвечены и закрыты.

Если хотя бы один пункт не выполнен — Request changes с указанием номера пункта.

### Разрешение конфликтов в коде

Если GitHub сообщает This branch has conflicts that must be resolved, автор переходит в свою ветку и получает изменения main:

```powershell
git checkout имя-вашей-ветки
git fetch origin
git merge origin/main
```

В конфликтующих файлах нужно найти блоки с маркерами <<<<<<<, =======, >>>>>>>, сохранить нужные изменения и удалить маркеры.

Затем добавить исправленный файл, создать коммит и отправить изменения:

```powershell
git add путь-к-исправленному-файлу
git commit -m "chore: resolve merge conflict with main"
git push
```

В командах имя-вашей-ветки и путь-к-исправленному-файлу заменяются фактическими значениями.

После новых коммитов approval сбрасывается. Автор нажимает Re-request review.

Конфликт не решается через git push --force.

## Защита ветки

Защищена ветка main.

Проверка прямого push:error: GH013: Repository rule violations found for refs/heads/main.

Проверка force-push:error: GH013: Repository rule violations found for refs/heads/main.

Ruleset protect-main:

- Enforcement status: Active.
- Bypass list: пустой.
- Target branches: Include default branch — main.
- Restrict deletions: включено.
- Block force pushes: включено.
- Require a pull request before merging: включено.
- Required approvals: 1.
- Dismiss stale pull request approvals when new commits are pushed: включено.
- Require conversation resolution before merging: включено.
- Require status checks to pass: выключено.
- Require linear history: выключено.

Automatically delete head branches включено.

Restrict deletions включено; на default-ветке экспериментом не проверяется.

Временное отключение защиты фиксируется в этом разделе: кто, когда и зачем отключал.

> TODO (модуль 3, практика №5): после появления CI-пайплайна включить в ruleset protect-main правило Require status checks to pass и добавить в список обязательных проверок джобы линтера и тестов. До этого момента зелёный пайплайн не является условием merge.

## Как запустить тесты

TODO (модуль 3): тестов пока нет, раздел появится вместе с ними.

## Встречи команды

- Частота: 2 раза в неделю.
- Канал связи: Telegram — https://t.me/+1G787niuVfUxMDIy
- Время ответа на сообщения: в течение 24 часов.

## Разрешение конфликтов

1. Обсуждение в команде.
2. Голосование большинством голосов.
3. Если не можем решить — обращаемся к преподавателю.

## Контакты

- Team Lead / Аналитик: Чувильчиков Кирилл — @cloynesssaa.
- Frontend / UI/UX: Судец-Ребров Арсений — @so1oface.
- Backend Developer: Редков Максим — @m4m_r4v.
- Desktop Developer: Булавин Данила — @danufe.

Канал команды: https://t.me/+1G787niuVfUxMDIy

Время ответа на сообщения: в течение 24 часов.
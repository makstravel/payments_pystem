# 💳 Payments System

Backend-сервис на Django, реализующий прием входящих webhook-уведомлений от банка и управление балансом организаций.

## 📌 Функциональность

- Прием POST-запросов от банка (`/api/webhook/bank/`)
- Защита от повторной обработки одной и той же операции (`operation_id`)
- Автоматическое начисление суммы на баланс организации по ИНН (`payer_inn`)
- Логирование изменения баланса (в консоль или таблицу)
- Подключение к базе данных MySQL
- Использование `.env` для хранения конфигурации

## 🚀 Быстрый старт

### 🔧 Установка зависимостей

```bash
pip install -r requirements.txt
```
### ⚙️ Настройка переменных окружения (.env)

```bash
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=...
```

### 🔄 Миграции и запуск

```bash
python manage.py migrate
```
```bash
python manage.py runserver
```

### 📨 Пример Webhook-запроса

POST /api/webhook/bank/

```bash
{
  "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
  "amount": 145000,
  "payer_inn": "1234567890",
  "document_number": "PAY-328",
  "document_date": "2024-04-27T21:00:00Z"
}
```
### Получение баланса по ИНН

GET /api/organizations/{INN}/balance/

```bash
{
  "inn": "1234567890",
  "balance": 145000
}
```

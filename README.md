# Telegram Bot with Django Admin

## Описание проекта
Простой Telegram-бот, который взаимодействует с базой данных и предоставляет администратору минимальный функционал через Django-админку.

## Инструкции по запуску
1. Клонируйте репозиторий.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Примените миграции:
   ```bash
   python3 manage.py migrate
   ```
4. Запустите сервер:
   ```bash
   python3 manage.py runserver
   ```
5. Запустите бота:
   ```bash
   python manage.py bot
   ```
### Ссылки
[Telegram-бот](https://t.me/qqroozatest_bot)
[Админка](https://127.0.0.1:8000/admin/)

#### Данные от админки находятся в корне проекта в файле `admin.txt`

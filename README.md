# Проект Foodgram

### Технологии
Python, Django, Docker

## О проекте
* Дипломный проеки Яндекс Практикума
* Сайт Foodgram, «Продуктовый помощник». Онлайн-сервис и API для него.
* На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд

## Авторы
* [Уманец Лилия](https://github.com/UmLilia)

### Запуск проекта в dev-режиме
- Клонировать репозиторий и перейти в него в командной строке.
- Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):
```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
```
- Затем нужно установить все зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
- Выполняем миграции:
```bash
python manage.py migrate
```
Создаем суперпользователя:
```bash
python manage.py createsuperuser
```
Запускаем проект:
```bash
python manage.py runserver
```

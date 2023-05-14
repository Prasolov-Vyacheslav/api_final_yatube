### Описание
Социальная сеть для публикации личных дневников, модуль API
### Технологии
Python 3.9

Django 3.2.16

Django Rest Framework 3.12.4

Djoser 2.1.0

### Запуск проекта в dev-режиме
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Prasolov-Vyacheslav/api_final_yatube.git
cd api_final_yatube
```
- Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
- Выполнить migrate
```
python manage.py migrate
```
- Создайте пользователя
```
python manage.py createsuperuser
```
- (или) Сменить пароль для пользователя admin
```
python manage.py changepassword admin
```
- Запуск сервиса
```
python manage.py runserver
```
### API Примеры
Создание токена
/api/v1/jwt/create/
{
    "username": "",
    "password": ""
}
### Документция ReDoc
```
https://redocly.github.io/redoc/
```
### Авторы
Прасолов Вячеслав

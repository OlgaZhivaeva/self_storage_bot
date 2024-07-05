# Пример админки склада

## Как установить

Установите виртуальное окружение

Выполните команды

```commandline
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Создайте суперпользователя

```commandline
python manage.py createsuperuser
```
Ваь потребуется ввести имя пользователя,
электронную почту и пароль.

Запуск

```commandline
python manage.py runserver
```
## Переменные окружения

Aдминка сайта http://127.0.0.1:8000/admin/

# Тестовое задания для Wildbox
## запуск через Docker
### У вас должен быть установлен и запущен Docker

Скопируйте проект командой 
 ```bash
git clone git@github.com:serapXXXD/test_task_for_wildbox.git
 ```
Перейдите в 
 ```bash
cd checker/checker_infra
 ```
Создайте .env файл
 ```bash
touch .env
 ```

Получите новый ключ джанго 
https://djecrety.ir/

Формат ключа:

```django-insecure-jvlf+slausy7o2#ak^%yji@p*g7lx(rxy4m23v1%+kwic_6ign```

Вам нужно заполнить .env по примеру

```bash
SECRET_KEY='django-insecure-(^+7^zp5&93u_#=u53dtd@@yirm8qfejt6hx*b(k8l5-hn*te6'
DEBUG=1
PRODUCTION=1

POSTGRES_ENGINE='django.db.backends.postgresql_psycopg2'   # НЕ МЕНЯТЬ!!!
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=database  # НЕ МЕНЯТЬ!!!
POSTGRES_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost

REDIS_HOST=redis
REDIS_PORT=6379
 ```
Пояснения:
 ```bash
До и после занка "=" пробелов быть не должно!

DJANGO_SECRET_KEY='django-insecure-Ваш ключ джанго Обязательно в одинарных ковычках!!!'

DEBUG=1 дебаг включен | 0 дебаг выключен

PRODUCTION=1 база даннных PostgreSQL | 0 SQLite


В параметре "ALLOWED_HOSTS" укажите список хостов слитно через запятую
 ```

Запускаем docker-compose

 ```bash
docker-compose up --build -d
 ```

 ```bash
docker ps
 ```

Должно быть запущенно 6 контейнеров
```bash
NAMES
checker_infra_celery_beat_1
checker_infra_nginx_1
checker_infra_backend_1
checker_infra_celery_worker_1
checker_infra_redis_1
checker_infra_database_1
```

Выполните 2 следущие команды
 ```bash
docker exec cism_infra_backend_1 python manage.py collectstatic --no-input

docker exec cism_infra_backend_1 python manage.py migrate
 ```

Примичание !
в данной сборке для работы с регистрацией и авторизацией пользователей используется 

```djoser==2.2.2 ```

докементация по djoser
https://djoser.readthedocs.io/en/latest/getting_started.html

### для создания пользователя 
на адрес 
```
.../auth/users/
```
отправьте POST запрос
```
{
    "username": "имя пользователя",
    "password": "пароль" 
}
```
все эндпоинты можно посмотреть по адресу 
```
.../swagger/
```


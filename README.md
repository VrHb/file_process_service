# Сервис для обработки файлов 


## Как запустить 

### Переменные окружения:

Создайте файл `.env`:

```
touch .env
```

1. Секретный ключ проекта: 

```
python manage.py shell
```

```
from django.core.management.utils import get_random_secret_key  

get_random_secret_key()
```

```
echo "DJANGO_SECRET_KEY=<сгенерированный ключ проекта>" >> .env
```

2. Название директории для статики

```sh
echo "STATIC_DIR_NAME=<название директории>"
```

> **Для развертывания проекта через docker необходимы две переменные окружения**
>
> ```
> echo "CELERY_BROKER=redis://redis:6379/0" >> .env && echo "CELERY_BACKEND=redis://redis:6379/0"
> ```

### Установка c помощью docker

```sh
docker-compose build && docker-compose up -d
```

### Установка вручную


#### Выполните миграции в БД

```sh
python manage.py migrate
```

#### Установите бд REDIS

```sh
sudo apt install redis
```

#### Запустите сервер

```sh
python manage.py runserver
```


#### Запустите celery worker

```sh
celery -A file_process_service worker --log-level=info
```


## Для тестирования

1. Endpoint для загрузки файла

```sh
curl -F 'file=@<путь к файлу>' http:/127.0.0.1:8890/upload/
```

2. Endpoint для просмотра загруженных файлов

```sh
curl <http://127.0.0.1:8890/files/>
```




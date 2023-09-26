# Сервис для обработки файлов 


## Как запустить 


#### Переменные окружения:

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
echo "DJANGO_SECRET_KEY='<сгенерированный ключ проекта>'" >> .env
```

2. Url для redis  

```sh
echo "REDIS_ENDPOINT='<url для REDIS>'" >> .env
```

3. Название директории для статики

```sh
echo "STATIC_DIR_NAME='<название директории>'"
```

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
pyton manage.py runserver
```


#### Запустите celery worker

```sh
celery -A file_process_service worker --log-level=info
```


## Для тестирования

1. Endpoing для загрузки файла

```sh
curl -F 'file=@<путь к файлу>' <http://url_сервера/upload/>
```

2. Endpoint для просмотра загруженных файлов

```sh
curl <http://url_сервера/files/>
```




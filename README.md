### Описание проекта
Проект API_YATUBE представляет собой сервис предоставляющий пользователям 
способ размещения своих мыслей в виде постов.
API реализован для всех функций сайта.
## Технологии 
Python, Django, Djoser, DRF

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Sherdiyor/api_final_yatube.git
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

```
cd yatube_api/
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Пример запросов
```
Пример get-запроса на endpoint posts
```

## Пример ответа
```
{
    "id": 1,
    "text": "string",
    "pub_date": "2024-03-24T14:15:22Z",
    "author": "string"
    "image": "string",
    "group": "1",
}
```
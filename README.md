# Weather Query Web Application

Это приложение позволяет получить информацию о текущей погоде для выбранного города и сохранить эти данные в базе данных PostgreSQL. Также приложение предоставляет страницу с историей запросов, где отображаются подробности о погоде для каждого запроса.

## Требования

Для успешной работы приложения нужно установить и настроить следующие компоненты:

- **Python 3.12+**
- **Django 5.1+**
- **PostgreSQL**
- **psycopg2** (или **psycopg2-binary**)

## Шаги по установке и запуску

### 1. Клонирование репозитория

Сначала клонируй репозиторий на свой локальный компьютер:

```bash
git clone https://your-repository-url.git
cd Weather_Query_Web_Application
```

### 2. Создание и активация виртуального окружения

Для изоляции зависимостей проекта, создайте виртуальное окружение и активируйте его:

```bash
python3 -m venv myenv
source myenv/bin/activate  # для Linux/Mac
myenv\Scripts\activate     # для Windows
```

### 3. Установка зависимостей

Установи все зависимости, указанные в `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Настройка базы данных

#### 4.1 Установка PostgreSQL

Если у тебя еще не установлен PostgreSQL, скачай и установи его с официального сайта: https://www.postgresql.org/download/

#### 4.2 Создание базы данных

Создай базу данных для проекта:

1. Подключись к PostgreSQL:

   ```bash
   psql -U postgres
   ```

2. Создай базу данных:

   ```sql
   CREATE DATABASE weather_db;
   ```

3. Создай пользователя (если нужно) и предоставь права:

   ```sql
   CREATE USER postgres WITH PASSWORD 'yourpassword';
   ALTER ROLE postgres SET client_encoding TO 'utf8';
   ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
   ALTER ROLE postgres SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE weather_db TO postgres;
   ```

#### 4.3 Настройка подключения к базе данных в `settings.py`

Открой файл **`settings.py`** и настрой параметры подключения к базе данных:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'weather_db',  # Имя базы данных
        'USER': 'postgres',    # Имя пользователя
        'PASSWORD': 'yourpassword',  # Пароль пользователя
        'HOST': 'localhost',   # Адрес хоста
        'PORT': '5432',        # Порт PostgreSQL
    }
}
```

### 5. Выполнение миграций

После того как база данных настроена, необходимо выполнить миграции, чтобы создать таблицы в базе данных:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Запуск приложения

Теперь ты можешь запустить сервер и проверить, что приложение работает:

```bash
python manage.py runserver
```

Приложение будет доступно по адресу **http://127.0.0.1:8000/**.

### 7. Просмотр истории запросов

Перейди по адресу **http://127.0.0.1:8000/weather-history/**, чтобы просмотреть список всех предыдущих запросов и данных о погоде.

---

## Структура проекта

```
Weather_Query_Web_Application/
├── manage.py
├── weather/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── Weather/
│           ├── index.html
│           └── weather_history.html
├── Weather_Query_Web_Application/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── requirements.txt
```

## Примечания

- Для работы с PostgreSQL убедись, что установлен пакет **`psycopg2`** или **`psycopg2-binary`**.


---

Эти шаги помогут тебе установить и настроить проект на локальной машине. Если возникнут вопросы или проблемы, не стесняйся спрашивать! 😊

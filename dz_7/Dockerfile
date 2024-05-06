# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.10

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Скопіюємо інші файли в робочу директорію контейнера
COPY "select_db.py" "select_db.py"
COPY "salary.db" "salary.db"
COPY "dz_6.py" "dz_6.py"
COPY "create_db.py" "create_db.py"
# Встановимо залежності всередині контейнера
RUN pip install -r requirements.txt

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 5432

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "dz_6.py"]

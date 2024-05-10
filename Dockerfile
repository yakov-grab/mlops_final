# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочий каталог приложения в контейнере
WORKDIR /usr/src/app

# Копируем файл requirements.txt в каталог нашего приложения
COPY requirements.txt ./

# Устанавливаем необходимые модули для Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения в контейнер
COPY . .

# Запускаем приложение
CMD [uvicorn src.api_app:app --host 0.0.0.0 --port 8091]

FROM python:3.12-slim


RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN chmod +x /app/docker/django/server-entrypoint.sh

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
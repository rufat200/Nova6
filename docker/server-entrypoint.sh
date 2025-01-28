#!/bin/sh

python manage.py
python manage.py collectstatic --noinput

exec gunicorn main.wsgi:application --bind 0.0.0.0:8000 --workers 4 --threads 4
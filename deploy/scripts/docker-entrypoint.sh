#!/bin/bash
set -e

if [ "$1" = 'gunicorn' ]; then
    echo "Create database migrations and apply"
    python manage.py makemigrations
    python manage.py migrate
fi

exec "$@"
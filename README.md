# Django 4 with PostgreSQL database

Python 3.10 Django project template to run as a Docker container using `gunicorn`.

## Getting Started

The Django app is packaged using a development Docker image as well as a production-ready build image. To start using/developing using this template, simply start the app stack using docker-compose to start postgresql and django with a volume mount for source files.

```
docker-compose up -d
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.2/) - The web framework used
* [psycopg2] - Database connector between Django and PostgreSQL
* [gunicorn](https://gunicorn.org/#docs) - WSGI server used to run Django
* [pytest](https://docs.pytest.org/en/stable/index.html) - Testing framework
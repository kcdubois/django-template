# Django 4 with PostgreSQL database

Python 3.10 Django project template to run as a Docker container using `gunicorn`.
## Built With

* [Django](https://docs.djangoproject.com/en/3.2/) - The web framework used
* [psycopg2](https://www.psycopg.org/docs/) - Database connector between Django and PostgreSQL
* [gunicorn](https://gunicorn.org/#docs) - WSGI server used to run Django
* [pytest](https://docs.pytest.org/en/stable/index.html) - Testing framework
---

## Getting Started

The Django app is packaged using a development Docker image as well as a 
production-ready build image. To start using/developing using this template, 
simply start the app stack using docker-compose to start postgresql and django 
with a volume mount for source files.


### 1. Generate a secret for Django
Use the helper script to generate a secret key that will be added to the 
environment variables of the Django app.
```bash
./deploy/scripts/generate_secret.sh
"nc_4y#1n_n=ttf*k5n7frbl3uk_7=9pg14g@ifilh6mrvj@d1g"
```

### 2. Create .env file for Compose to reference
Create a `.env` file at the root of the project to configure environment 
variables for the Django app, with the following as minimum:

```bash
#! /.env
DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=django
SECRET_KEY=nc_4y#1n_n=ttf*k5n7frbl3uk_7=9pg14g@ifilh6mrvj@d1g
DEBUG=yes
```

### 3. Start the development server
Use the helper script to start the development server using Compose and setting 
up the context and project name appropriately.
```
./deploy/scripts/start_dev.sh
```
---
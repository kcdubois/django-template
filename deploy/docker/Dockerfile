FROM python:3.10.8-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential gcc python3-dev musl-dev \
    postgresql-server-dev-all libintl-perl gettext &&\
    pip install pipenv

COPY Pipfile Pipfile.lock ./


FROM base as development
RUN pipenv sync --system --dev
COPY app .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM base as builder
RUN mkdir /wheels && \
    pipenv requirements > /wheels/requirements.txt && \
    pip wheel -r /wheels/requirements.txt -w /wheels


FROM python:3.10.8-slim

COPY --from=builder /wheels /wheels
RUN pip install --no-index -r /wheels/requirements.txt -f /wheels

RUN rm -rf /wheels

COPY ./deploy/scripts/docker-entrypoint.sh /docker-entrypoint.sh
WORKDIR /app
COPY app .

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["gunicorn", "-b 0.0.0.0:8000", "-w 3", "app.wsgi"]
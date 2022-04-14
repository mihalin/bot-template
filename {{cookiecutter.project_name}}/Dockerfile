FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.12 \
    POETRY_VIRTUALENVS_CREATE="false"

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock docker-entrypoint.sh ./
RUN poetry install --no-interaction --no-ansi --no-dev

COPY {{cookiecutter.project_name}} /app

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]

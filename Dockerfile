FROM python:3.11-slim-buster

EXPOSE 8000

RUN pip install poetry==1.6.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN poetry install --no-dev --no-root && rm -rf $POETRY_CACHE_DIR

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY rest_services ./rest_services

CMD ["uvicorn", "rest_services.main:app", "--host", "0.0.0.0", "--port", "80"]

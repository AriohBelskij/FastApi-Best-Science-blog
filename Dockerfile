FROM python:3.11.6-slim-bullseye

LABEL maintainer="eugeneyakim4@google.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /project

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir --upgrade poetry

COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    mv .env .env_temp && \
    poetry run python -m dotenv -f .env_temp .env && \
    rm .env_temp

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
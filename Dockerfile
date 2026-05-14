FROM ghcr.io/astral-sh/uv:python3.14-alpine

WORKDIR /app

ENV UV_SYSTEM_PYTHON=1
ENV UV_COMPILE_BYTECODE=1
ENV UV_NO_DEV=1
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY . .

COPY /scripts/run_migration.sh .
RUN chmod +x run_migration.sh

ENTRYPOINT ["./run_migration.sh"]

CMD ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "8000", "--workers", "2", "src.main:app"]

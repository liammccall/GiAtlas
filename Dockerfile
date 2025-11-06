FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false

# --- Install curl and Poetry ------------------------------------
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

#Path for Poetry
ENV PATH="/root/.local/bin:$PATH"


# --- Set working directory inside the container ------------------
WORKDIR /src/python

# --- Copy dependency files first (for Docker cache) --------------
COPY src/python/pyproject.toml src/python/poetry.lock* ./

# --- Install deps ------------------------------------------------
RUN poetry install --no-interaction --no-ansi

# --- Copy actual app code afterwards -----------------------------
COPY src/python/ ./

# --- Default CMD -------------------------------------------------
CMD ["python", "-c", "print('hello world')"]
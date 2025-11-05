FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_CREATE=false

# System deps:
RUN curl -sSL https://install.python-poetry.org | python3 -

CMD ["python", "-c", "print('hello world')"]
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim-bookworm

EXPOSE 5002

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Poetry config
ENV POETRY_VIRTUALENVS_CREATE=false

#Install curl
RUN apt-get update && \
    apt-get install -y curl

#Install gunicorn
RUN apt-get install -y gunicorn
    
# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PATH="/root/.local/bin:${PATH}"

# Install pip requirements
COPY pyproject.toml poetry.lock README.md ./
RUN poetry install

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "src.python.main:app"]

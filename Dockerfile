# pull official base image
FROM python:3.12-slim

# set work directory
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install poetry
ENV POETRY_VERSION=1.7.0
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY ./pyproject.toml ./poetry.lock* /src/

# install system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd

# install dependencies:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

# copy entrypoint.sh
COPY src/entrypoint.sh .
RUN sed -i 's/\r$//g' .//entrypoint.sh
RUN chmod +x ./entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
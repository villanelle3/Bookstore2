# `python-base` sets up all our shared enviroment variables
FROM python:3.10-slim as python-base

# python:
ENV PYTHONUNBUFFERED=1 \
  # prevents python from creating .pyc files
  PYTHONDONTWRITEBYTECODE=1 \
  \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  \
  # poetry:
  POETRY_VERSION=1.7.1 \
  # make poetry install to this location
  POETRY_HOME="/opt/poetry" \
  # make poetry create the virtual enviroment in the project's root
  # it gets named `.venv`
  POETRY_VIRTUALENVS_IN_PROJECT=true \
  # do not ask any interactive question
  POETRY_NO_INTERACTION=1 \
  \
  # paths
  # this is where our requirements + virtual enviroment will live
  PYSETUP_PATH="/opt/pysetup/" \
  VENV_PATH="/opt/pysetup/.venv"


# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# `builder-base` stage is used to build deps + create our virtual enviroment
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        # deps for installing poetry
        curl \
        # deps for building python deps
        build-essential


# install poetry - respects $POETRY_VERSION & POETRY_HOME
RUN pip install poetry


# install postgres dependencies
RUN apt-get update \
  && apt-get -y install libpq-dev gcc \
  && pip install psycopg2

# copy project requirement files here to ensure they will be cached
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./


# install project requirements
RUN poetry install --no-root


WORKDIR /app
COPY . /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
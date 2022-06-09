# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.development
ENV READ_DOT_ENV_FILE=True
ENV ENV_FILE=../environments/development.env
ENV DEBUG=False

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

WORKDIR /usr/src/bnbdj

COPY ../../requirements/development.txt /

RUN pip install -r ../requirements/development.txt

#COPY /compose/dev/start /start
#RUN sed -i "s/\r$//g" /start  #
#RUN chmod +x /start  # add permission to make it executable

COPY ../.. /

CMD ["./runserver.sh"]




# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app
COPY ./Pipfile.lock /usr/src/app

RUN pipenv install --system --ignore-pipfile

# copy project
COPY . /usr/src/app

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# run server
#USER root
#RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
CMD ["/bin/bash", "/usr/src/app/entrypoint.sh"]

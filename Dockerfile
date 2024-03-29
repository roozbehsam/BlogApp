# syntax=docker/dockerfile:1
FROM python:3.10.6
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install pipenv
COPY ./Pipfile* /tmp/
RUN cd /tmp && pipenv requirements > requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
WORKDIR /code

# It is not required to copy the directory since we are using compose
#COPY . .
FROM python:3.7-alpine
MAINTAINER Oguzhan Celikarslan

ENV PYTHONUNBUFFERED 1

# left requirements.txt specify the file which at the same index with Dockerfile. Right is the path in docker.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# we are going to create a user who is going to run our application using docker.
# we made it for security proposes.
RUN adduser -D user
USER user
FROM python:3.8.0a3-alpine

# Allows python to run outputs unbuffered
ENV PYTHONUNBUFFERED 1

# Install reqirements for the backend
COPY ./requirements.txt /requirements.txt 
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Copy the source code to the docker image
RUN mkdir /Src
WORKDIR /Src
COPY ./Src /Src

# Create a new user to run the backend, so it will not be run by root
# This is done to reduce damage if the container is compromised
RUN adduser -D backendRunner
USER backendRunner

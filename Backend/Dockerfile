FROM python:3.8-buster

# Allows python to run outputs unbuffered
ENV PYTHONUNBUFFERED 1

# Install reqirements for the backend
COPY ./requirements.txt /requirements.txt 
RUN pip install -r /requirements.txt

# Copy the source code to the docker image
RUN mkdir /Src
WORKDIR /Src
COPY ./Src /Src
COPY ./pytest.ini /pytest.ini

# Create a new user to run the backend, so it will not be run by root
# This is done to reduce damage if the container is compromised
RUN useradd backendRunner
USER backendRunner

FROM node:8.15.1-alpine

EXPOSE 8080

RUN mkdir Frontend
WORKDIR /Frontend

# Install requirements on container from package.json
COPY ./package.json /Frontend/package.json
RUN yarn install

COPY . Frontend

# Create a new user to run the frontend, so it will not be run by root
# This is done to reduce damage if the container is compromised
RUN adduser -D frontendRunner
USER frontendRunner

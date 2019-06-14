#!/bin/bash

# This is a simple script to run linting and test
# with docker-compose  on  frontend and backend 

echo "-----------RUNNING BACKEND TESTS-----------"
docker-compose run backend sh -c "pytest"
echo "-----------RUNNING FONTEND TESTS-----------"
docker-compose run frontend sh -c "yarn run test"
echo "-----------RUNNING BACKEND LINTING -----------"
docker-compose run backend sh -c "flake8"
echo "-----------RUNNING FRONTEND LINTING -----------"
docker-compose run frontend sh -c "yarn run eslint"
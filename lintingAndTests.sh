#!/bin/bash

# This is a simple script to run linting and test
# with docker-compose  on  frontend and backend 

echo "----------- BUILDING CONTAINERS -----------"
docker-compose build
echo "-----------RUNNING BACKEND TESTS-----------"
docker-compose run backend sh -c "python manage.py test"
docker-compose run backend sh -c "python -m pytest GameEngine/tests/"
echo "-----------RUNNING FONTEND TESTS-----------"
docker-compose run frontend sh -c "yarn run test"
echo "-----------RUNNING BACKEND LINTING -----------"
docker-compose run backend sh -c "flake8"
echo "-----------RUNNING FRONTEND LINTING -----------"
docker-compose run frontend sh -c "yarn run eslint"
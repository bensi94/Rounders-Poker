[![Build Status](https://travis-ci.com/bensi94/Rounders-Poker.svg?branch=master)](https://travis-ci.com/bensi94/Rounders-Poker)

# Rounders - Online Poker platform

## (WORK IN PROGRESS)

This project is currently a work in progress.  
**Current stage:** All current project setup should be done, docker containers, Recat frontend, Django backend with all test suites and tools ready, and postgresql database has been set up. Users are able to signup, log in and log out. Authentication token is saved in cookies, and logged in users have different access rights then those that are not.

![App profile](https://github.com/bensi94/Rounders-Poker/blob/master/app-profile.png)

## Running the application  

Only dependency to run the application is Docker.  
To build the application run:
`docker-compose build && docker-compose up`  

### Frontend

The frontend will run on port 8080 (can be changed in docker-compose file).  
[localhost:8080](http://localhost:8080)

### Backend
The backend will run on port 8000 (can be changed in docker-compose file).  
[localhost:8000](http://localhost:8000)  

**Valid Routes:**
*  [/admin](http://localhost:8000/admin) - Login as superuser(admin)
*  [/api/user/create](http://localhost:8000/api/user/create) - Create user
*  [/api/user/me](http://localhost:8000/api/user/me) - Used to update user (needs token for authorization)
*  [/api/user/token](http://localhost:8000/api/user/token) - Returns the token of user on valid user data

**Create superuser:**  
Command:  
`docker-compose run backend sh -c "python manage.py createsuperuser"`  
It will ask you for username and password. From there you can create, delete and change users.

##  Project Design and Technology 


### Frontend 

* Created with React
* Configured with webpack and babel
* Tested with jest and linting with eslint

### Backend

* Created with Django
* Tested with Pytest and Django
* PostgreSQL

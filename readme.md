# How to use

## build and test

building a docker image will execute tests

> docker build . -t loantest

## run

run a webserver on 8080

> docker run -it --name loancontainer -p 8080:8080 loantest ./manage.py runserver

## apply db migrations

> docker exec -it loancontainer ./manage.py migrate --no-input

## create superuser account

use this superuser account to create admins

> docker exec -it loancontainer ./manage.py createsuperuser

## run with postgres

run the docker container with environment variables needed to connect to postgres(look at .env.example).

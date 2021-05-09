# How to use

## build and test

> docker build . -t loantest

## run

> docker run -it --name loancontainer -p 8080:8080 loantest ./manage.py runserver

## apply db migrations

> docker exec -it loancontainer ./manage.py migrate --no-input

## create superuser account

> docker exec -it loancontainer ./manage.py createsuperuser

## run with postgres

run the docker container with environment variables needed to connect to postgres(look at .env.example).

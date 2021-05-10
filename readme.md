# How to use

## build and test

The repository is configured to automatically run tests on push to master.

also, building a docker image will execute tests during the image build

> docker build . -t loantest

## run

run a webserver on 8080

> docker run -it --name loancontainer -p 8080:8080 loantest

## apply db migrations

> docker exec -it loancontainer ./manage.py migrate --no-input

## create superuser account

use this superuser account to create admins

> docker exec -it loancontainer ./manage.py createsuperuser

## run with postgres

by default this app runs on sqlite3 database inside the container filesystem,
you can also run the docker container with postgreSQL,
add the environment variables needed to connect to postgres(look at .env.example).

## run without docker

To run locally setup the dependencies in your virtualenvironment by

> pip install -r requirements.txt

to run tests

> pytest

apply database migrations

> ./manage.py migrate --no-input

collect staticfiles(for swagger ui api docs)

> ./manage.py collectstatic --no-input

start the server by

> ./manage.py runserver 0.0.0.0:8080

Api documentation will be available on `0.0.0.0:8080`

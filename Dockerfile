FROM python:3.8-alpine 

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

EXPOSE 8080

# psycopg2 for postgres
RUN apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip3 install --no-cache-dir psycopg2 psycopg2-binary  

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ADD . .

RUN ./manage.py collectstatic --no-input

RUN pytest  # run tests

ENTRYPOINT [ "python3" ]

CMD ["./manage.py","runserver","0.0.0.0:8080"]
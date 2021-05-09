FROM python:alpine

WORKDIR /app

EXPOSE 8080

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ADD . .

RUN ./manage.py test  # run tests

CMD ["./manage.py","runserver","0.0.0.0:8080"]
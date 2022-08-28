FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add build-base \
    && pip install -r requirements.txt

ADD main.py /

COPY . /app

EXPOSE 5000

CMD ["python", "main.py", "--host=0.0.0.0"]
FROM python:3.7-alpine

COPY . /app
WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_DEBUG 1
ENV FLASK_ENV development

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

CMD ["flask", "run"]
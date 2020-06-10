FROM python:3.7-alpine

WORKDIR /usr/src/app/

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_DEBUG 1
ENV FLASK_ENV development
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
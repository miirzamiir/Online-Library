FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir app
WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .
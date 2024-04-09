# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app
CMD black /app/*.py
CMD [ "python3", "src/helloworld/HelloWorld.py"]
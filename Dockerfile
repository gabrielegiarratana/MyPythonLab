# syntax=docker/dockerfile:1

FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt  \
# NB: in a windows environment, path should be written with "\" like RUN powershell New-Item c:\\test or
# RUN ["powershell", "New-Item", "c:\test"]

COPY . /app
CMD black /app/*.py
CMD [ "python3", "src/helloworld/HelloWorld.py"]
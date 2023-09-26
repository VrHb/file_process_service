FROM python:3.9.6-alpine

WORKDIR /usr/src/app

RUN pip install -U pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . ./ 

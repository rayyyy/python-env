FROM python:3.10-buster
COPY requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /app
COPY . /app
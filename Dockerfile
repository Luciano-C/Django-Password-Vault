FROM python:3.9

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .


RUN pip install --upgrade pip && pip3 --no-cache-dir install -r requirements.txt



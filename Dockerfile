FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app


RUN pip3 --no-cache-dir install -r requirements.txt


EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]
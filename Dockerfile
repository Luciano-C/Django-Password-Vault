FROM python:3.9

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .


RUN pip install --upgrade pip && pip3 --no-cache-dir install -r requirements.txt


EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
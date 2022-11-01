## To run
$ virtualenv venv <br>
$ pip install -r requirements.txt <br>
$ . venv/Scripts/activate <br>
$ python manage.py runserver



Para correr en docker

$ sudo docker compose up
En otra terminal
$ sudo docker exec -it password-vault-image bash
$ python manage.py runserver 0.0.0.0:8000 
## <ins>To run locally</ins>
A .env file with the following variables is required at the root folder:

### <ins>Django</ins>
SECRET_KEY=DjangoSecretKey

### <ins>MySQL Database</ins>
DB_USER=Your_User <br>
DB_PASSWORD=Your_Password <br>
DB_HOST=Your_Host (Can be "localhost") <br>
DB_PORT=3306 <br>
DB_NAME=Name_For_MySQL_Database 



### <ins>Commands on terminal</ins>
\$ virtualenv venv <br>
\$ pip install -r requirements.txt <br>
\$ . venv/Scripts/activate <br> 
\$ python manage.py migrate <br>
\$ python manage.py runserver 



## <ins>To run in Docker</ins>
Change the value DB_HOST=Your_Host to DB_HOST=db

You also need the following variables added to .env

MYSQL_ROOT_PASSWORD=Your_Password <br>
MYSQL_DATABASE=Name_For_MySQL_Database <br>

Note that you could use the variables the values for DB_PASSWORD and DB_NAME here and you could also just use these variables to run locally.<br>
In this case you would need to update the variable DATABASE in settings.py as follows: <br>

DATABASES = {
    'default': dj_database_url.config(default=f"mysql://{os.environ.get('DB_USER')}:{os.environ.get('MYSQL_ROOT_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('MYSQL_DATABASE')}")
} 
<br>
<br>
In my case I wanted to keep them separated this time so I could keep better track of which environment variables were needed for the Django app and which for Docker.

### <ins>Commands on terminal</ins>
\$ sudo docker compose up ($ sudo docker compose up --build)
Sometimes you can are ready to go, but most of the time the database won't be ready when the container for the app is, so in another terminal you can use the following: <br>
\$ sudo docker exec -it password-vault bash <br>
\$ python manage.py runserver 0.0.0.0:8000 <br>
# django_mongodb
Project using django, DRF and mongodb

## Requisites
* Python3.7
* mongodb

#### Can be executed with Docker
* Docker
* docker-compose

### For run with docker
In the root folder execute
```
docker-compose up
```
Maybe ***sudo*** could be required. This command will start the container, download the images of python3.7 and mongodb.
Also will configure the project with the Dockerfile, setting enviroment variables to mongodb configuration and run all extra commands for install extra libraries, make migrations and execute the server in port 8000

## Note
All next steps are for a manual configuration of the project. For do this, is also required create and activate a ***virtualenv*** with python3.7 and have installed mongodb

All extra libraries are save in ***requirements.txt*** file. This is also executed by the Dockefile, but for run manually execute
```
pip install requirements.txt
```

Make migrations
```
python manage.py makemigrations
```
Migrate models
```
python manage.py migrate
```
Before running the server be sure of configuring the variables for the connection with mongodb. Edit variable DATABASES in the file **settings.py** inside **django_mongodb** folder
```
DATABASES = {
   'default' : {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'NAME': <databasename>,
        'HOST': <host>,
        'PORT': 27017,
        'USER': <username>,
        'PASSWORD': <password>,
   }
}
```
Last setp. Run the server
```
python manage.py runserver
```

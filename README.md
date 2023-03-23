# Practical task 2 week

# Manual
### 1 install Postgresql
### 2 install Django framework, Requests, Rest Framework
#### pip instal django requests djangorestframework 
### 3 change database settings in settings.py
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user'(default is 'postgres'),
        'PASSWORD': 'your_password',
        'HOST': 'your_host'(default is 'localhost'),
        'PORT': 'your_port'(default is '5432'),
    }
### 4 migrate data model to database
#### python manage.py makemigrations
#### python manage.py migrate
### 5 run
#### python manage.py runserver

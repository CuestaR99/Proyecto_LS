<p align="center">
  <a href="https://www.djangoproject.com" target="blank"><img src="https://icon-library.com/images/django-icon/django-icon-0.jpg" width="200" alt="Nest Logo" /></a>
</p>

## Requirements.

* [Python](https://www.python.org) Requerimientos necesarios.
```Python 3.11.3 o superior```

## Install Django.
[Install Django](https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release).

```bash
$ python -m pip install Django
```

## Creatin a Project.
[Documentation Djago](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
```bash
# Crear nuevo proyecto.
$ django-admin startproject 'Project-name'

# Crear apliacion
$ python manage.py startapp 'new-model'
```
## The development server.

```bash
# Iniciar Servidor de desarrollo
$ python manage.py runserver
```

## Database setup
[Database Django](https://docs.djangoproject.com/en/4.2/intro/tutorial02/)

<p>Por defecto, Django usa la configuracion de SQLite, la cual esta incluida en Python<p>

```bash
#Buscar Cambios para realizar migraciones
$ python manage.py makemigrations

#Realizar migraciones
$ python manage.py migrate
```

## Conneting to the database
```bash
#Configuracion para MySQL
$ settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',        
    }
}

#install mysqlclient
$ pip install mysqlclient
```
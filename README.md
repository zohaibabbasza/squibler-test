# Introduction

The goal for this project is to create a collaborative editor using django rest framework


### Version

* Python 3.9

* Django 4.0.2

* Django Rest Framwork 3.13.1

* SQLite by default if no env variable is set

# Usage

To use this template to start your own project:

### Creating virtualenv
    $ python3.9 -m venv venv \
    source venv/bin/activate
      
      
After that just install the local dependencies, install libraries.

### Installing Libraries

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install -r requiremnts.txt

    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

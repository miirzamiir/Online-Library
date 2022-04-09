#  Online Library
***

This is a training project which is an implementation of an online library API. The installation instructions are written bellow.

## installation
- - - 
 after cloning project do these instructions step by step.
###  1-  create a virtual environment and activate it.
```
python -m venv ./venv
source ./venv/bin/activate 
```
### 2- create a sqlite file.
``` touch lib.sqlite3 ```  
  
you can also use other database engines but you have to change `OnlineLibrary/settings.py` module.
 
### 3- install requirements.
``` pip install -r ./requirements.txt ```
### 4- run migrations.
``` python manage.py migrate```
### 5- start server and use the api.
``` python manage.py runserver ```

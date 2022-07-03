#  Online Library
An online library management system api written with python, django and DRF.

# Tools
  - python
  - django
  - django rest framework
  - docker
  - postgresql(as default database)


# Installation
 after cloning project do these instructions step by step.
After cloning project, you can simply run this project by following instructions bellow.

### 1- environment variables.
create a `.env` file and set value for `SECRET_KEY`, `POSTGRES_NAME`, `POSTGRES_USER` and `POSTGRES_PASSWORD` keys.
### 2- install docker and docker-compose.
you can install docker from [here](https://docs.docker.com/engine/install/).

### 3- docker commands.
open a terminal and run command bellow.
```
docker-compose up
```
this command will run project on `localhost:8000` and you will be able to visit that by your favorite browser.

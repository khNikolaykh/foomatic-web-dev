foomatic-web-dev
================

First go at a redesigned website for the Foomatic Hackerspace

Pre-requisites
==============
* Python >= 2.7
* virtualenv
* pip
* Postgresql
* git

Instructions for setting up and testing the project
---------------------------------------------------

1. Create the virtual env: 

    * virtualenv FooWeb
    * cd FooWeb
    * source bin/activate

2. clone the project repository:
    
    * git clone git://github.com/tmcqueen/foomatic-web-dev.git
    * cd foomatic-web-dev
    * pip install -r reqs.txt

3. create the database

    * createdb fooweb

4. update the database from the models

    * python manage.py syncdb

5. run the development server:

    * ./start.sh

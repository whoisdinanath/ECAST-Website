#!/usr/bin/bash
python3 manage.py makemigrations $1
python3 manage.py migrate $1
python3 manage.py runserver






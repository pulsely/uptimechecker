#!/bin/sh

source ./venv/bin/activate
source .env

python manage.py runserver

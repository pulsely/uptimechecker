#!/bin/sh

source ./venv/bin/activate
source .env
celery -A uptimechecker worker -B -l INFO

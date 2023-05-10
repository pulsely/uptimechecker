.DEFAULT_GOAL := dev

dev:
	source ./venv/bin/activate ;  python manage.py runserver

test:
	python manage.py test

reset:
	python manage.py reset

celery:
	source ./venv/bin/activate ; source .env ; celery -A uptimechecker worker -B -l INFO

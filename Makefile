.DEFAULT_GOAL := dev

dev:
	python manage.py runserver

test:
	python manage.py test

reset:
	python manage.py reset


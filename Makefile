run:
	poetry run python manage.py runserver

requirements:
	poetry export -f requirements.txt --output requirements.txt

locale:
	poetry run django-admin makemessages -l ru

compile:
	poetry run django-admin compilemessages --ignore=env

makemigrations:
	poetry run python3 manage.py makemigrations

makemigrations_users:
	poetry run python3 manage.py makemigrations users

migrate:
	poetry run python3 manage.py migrate

.PHONY: run

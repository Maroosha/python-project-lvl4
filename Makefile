run:
	poetry run python manage.py runserver

requirements:
	poetry export -f requirements.txt --output requirements.txt

locale:
	poetry run django-admin makemessages -l ru

lint:
	poetry run flake8 task_manager

compile:
	poetry run django-admin compilemessages --ignore=env

makemigrations:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

makemigrations_users:
	poetry run python3 manage.py makemigrations users
	poetry run python3 manage.py migrate

makemigrations_statuses:
	poetry run python3 manage.py makemigrations statuses
	poetry run python3 manage.py migrate

makemigrations_tasks:
	poetry run python3 manage.py makemigrations tasks
	poetry run python3 manage.py migrate

makemigrations_labels:
	poetry run python3 manage.py makemigrations labels
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

.PHONY: run test locale

run:
	poetry run python manage.py runserver

requirements:
	poetry export -f requirements.txt --output requirements.txt

locale:
	poetry run django-admin makemessages -l ru

.PHONY: run

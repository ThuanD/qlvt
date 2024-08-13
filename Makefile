init:
	pip install -r requirements.txt

key:
	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

migrate:
	python manage.py migrate

static:
	python manage.py collectstatic --no-input

run:
	python manage.py runserver

gunicorn:
	gunicorn app.wsgi:application -b 0.0.0.0:8000

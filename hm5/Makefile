include .env_dev

loadEnvs:
	exit 1
	source .env_dev

run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

createApp:
	@read -p "Enter name:" name ; \
	python manage.py startapp $$name

freeze:
	python -m pip freeze > requirements.txt

runDb:
	 docker compose up

createAdmin:
	python manage.py createsuperuser

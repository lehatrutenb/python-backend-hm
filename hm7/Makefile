include .env_dev

run:
	docker compose build
	docker compose up

stop:
	docker compose down

loadEnvs:
	exit 1
	source .env_dev

runServer:
	python manage.py runserver 0.0.0.0:8000

runDb:
	docker compose build
	docker compose up postgres

runTest:
	python manage.py test --noinput

runServerWithMigrate: migrate runServer

migrate:
	python manage.py makemigrations
	python manage.py migrate

unmigrateMessangerApp:
	@read -p "Enter name of migration to return to (ex: 0001_initial):" name ; \
	python manage.py migrate messangerApp $$name

createApp:
	@read -p "Enter name:" name ; \
	python manage.py startapp $$name

freeze:
	python -m pip freeze > requirements.txt

unfreeze:
	pip install -r ./requirements.txt

createAdmin:
	python manage.py createsuperuser

fillDBWithRandomDataCommand:
	python manage.py data_base_mock_fill

fillDBWithRandomDataMigration: migrate

clearDBData:
	exit 1
	docker volume rm  hm6_pg_messanger_data


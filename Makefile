# Makefile for fromily-server

build:
	docker-compose build

update_dep:
	docker-compose run web pip3 freeze > requirements.txt

run:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate
	docker-compose up

# open an interactive shell
open:
	docker-compose run web bash
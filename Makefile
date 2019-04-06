# Makefile for fromily-server

update_dep:
	docker-compose run web pip3 freeze > requirements.txt

run:
	docker-compose up

# open an interactive shell
open:
	docker-compose run web bash

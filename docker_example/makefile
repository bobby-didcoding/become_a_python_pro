ifneq (,$(wildcard ./.env))
	include .env 
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose up -d --build --remove-orphans

enter_python:
	docker exec -it python bash



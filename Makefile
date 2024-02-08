#!/bin/bash

# Run the application in local environment
run_debug: venv
	@. venv/bin/activate && python3.11 src/main.py

# Install in local environment
venv: .env
	@python3.11 -m venv venv
	@. venv/bin/activate && pip install -r requirements.txt

# Install in docker
docker: .env
	@docker compose up -d

.env:
	@cp .env.dev .env

clean_local_install:
	@rm -rf venv

# docker commands
docker_restart: #restart container
	@docker compose restart

docker_clean: #clean container
	@docker compose down --rmi all --volumes --remove-orphans

docker_up: #start container
	@docker compose up -d

docker_rebuild: #rebuild container
	@docker compose up --force-recreate --build -d

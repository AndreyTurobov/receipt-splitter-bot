.PHONY: all

SHELL=/bin/zsh -e
STORAGES=docker-compose/storages.yaml

lint:
	poetry run ruff check --fix .

format:
	poetry run ruff format .

db-up:
	docker-compose --env-file .env -f $(STORAGES) up -d

db-down:
	docker-compose --env-file .env -f $(STORAGES) down
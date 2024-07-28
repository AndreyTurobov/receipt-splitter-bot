.PHONY: all

SHELL=/bin/zsh -e

lint:
	poetry run ruff check --fix .

format:
	poetry run ruff format .
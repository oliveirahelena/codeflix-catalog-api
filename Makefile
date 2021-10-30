# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

SHELL := /bin/bash

setup:
	python -m venv .venv
	( \
       source .venv/bin/activate; \
       pip install -r requirements/dev.txt; \
	   pre-commit install; \
    )

unit-tests:
	.venv/bin/python -m pytest -svv /tests/unit --cov=src --cov-report=term-missing

black:
	.venv/bin/python -m black -l 86 $$(find * -name '*.py')

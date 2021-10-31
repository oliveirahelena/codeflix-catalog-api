# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

SHELL := /bin/bash
PYTHON = .venv/bin/python

define PYSCRIPT_CREATEDB
print("Aqui vai o script de criar o banco de dados")
endef

CREATEDB =: $(shell ${PYTHON} -c '$(PYSCRIPT_CREATEDB)')

setup:
	python -m venv .venv
	( \
       source .venv/bin/activate; \
       pip install -r requirements/dev.txt; \
	   pre-commit install; \
    )

unit-tests:
	${PYTHON} -m pytest -svv /tests/unit --cov=src --cov-report=term-missing

black:
	${PYTHON} -m black -l 86 $$(find * -name '*.py')

create_db:
	echo $(CREATEDB)

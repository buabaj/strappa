[.PHONY: test
test:
	python3 -m pytest

.PHONY: ruff
ruff:
	python3 -m ruff check --output-format=full

.PHONY: ruff-fix
ruff-fix:
	python3 -m ruff check --fix

.PHONY: mypy
mypy:
	python3 -m mypy ./src --check-untyped-defs

.PHONY: format
format:
	python3 -m ruff format

.PHONY: lint
lint: ruff mypy

.PHONY: coverage
coverage:
	python3 -m pytest --verbose --cov=.

.PHONY: coverage-report
coverage-report:
	python3 -m pytest --verbose --cov=. --cov-report=html

.PHONY: all_checks
all_checks: format ruff-fix lint test ]
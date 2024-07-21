venv: requirements.txt
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt

PHONY: fmt
fmt:
	trunk fmt

PHONY: check
check:
	trunk check

PHONY: check-all
check-all:
	trunk check --all

PHONY: pytest
pytest: venv
	venv/bin/pytest

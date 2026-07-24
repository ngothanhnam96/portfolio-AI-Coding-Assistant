.PHONY: install lint test run docker-build ci

install:
	python -m pip install -r requirements-dev.txt

lint:
	ruff check .

test:
	pytest

run:
	uvicorn app.main:app --reload

docker-build:
	docker build -t ai-coding-assistant:local .

ci: lint test

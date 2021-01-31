.DEFAULT_GOAL := help

.PHONY: tests run install clean generate-configuration

tests: ## Run all tests
	usr/bin/python3 -m pytest -s tests/*

run: ## Run dca algorithm and buy bitcoin in kraken platform
	python3 main.py

install: ## Install dependencies
	pip3 install -r requirement.txt

clean: ## clean db files:
	rm db/*db*

generate-configuration: ## create dca configuralion json file:
	cp dca_configuration.json dca_configuration_production.json

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

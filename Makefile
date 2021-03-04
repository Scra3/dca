.DEFAULT_GOAL := help

.PHONY: tests run install clean-db generate-configuration run-production backup-db projection

BACKUP_DIRECTORY := $(shell date +%Y-%m-%d.%H:%M:%S)

tests: ## Run all tests
	python3 -m pytest -s tests/*

run: ## Run dca algorithm and buy bitcoin in kraken platform
	python3 main.py

run-production: ## Run dca algorithm in production mode
	export ENV=production && python3 main.py

install: ## Install dependencies
	pip3 install -r requirement.txt

clean-db: ## clean db files:
	rm db/*db*

backup-db: ## backup db files:
	mkdir -p backup; mkdir backup/$(BACKUP_DIRECTORY) && cp db/* backup/$(BACKUP_DIRECTORY)/ && echo "backup done"

generate-configuration: ## create dca configuration json file
	cp dca_configuration.json dca_configuration_production.json

projection: ## do a projection to estimate configuration parameters
	python3 projection.py

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

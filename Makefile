.DEFAULT_GOAL := help

.PHONY: tests run install clean-db generate-configuration run-production backup-db projection run-front copy-data-to-front

BACKUP_DIRECTORY := $(shell date +%Y-%m-%d.%H:%M:%S)

tests: ## Run all tests
	python3 -m pytest

run: ## Run dca algorithm and buy bitcoin in kraken platform
	python3 main.py

run-front: ## Display graph
	cd front/chart && npm run serve

run-production: ## Run dca algorithm in production mode
	export ENV=production && python3 main.py

install: ## Install dependencies
	pip3 install -r requirements.txt

clean-db: ## clean db files:
	rm db/*db*

lint-fix: ## apply lint:
	python3 -m black . && python3 -m isort . && python3 -m mypy .

backup-db: ## backup db files:
	mkdir -p backup; mkdir backup/$(BACKUP_DIRECTORY) && cp db/* backup/$(BACKUP_DIRECTORY)/ && echo "backup done"

generate-configuration: ## create dca configuration json file
	cp dca_configuration.json dca_configuration_production.json

projection: ## do a projection to estimate configuration parameters
	python3 projection.py

copy-data-to-front: ## copy data to display in front
	rm -rf ./front/chart/data
	mkdir ./front/chart/data
	cp db/* ./front/chart/data/
	cp dca_configuration_*.json ./front/chart/data/configuration.json
	mv ./front/chart/data/log* ./front/chart/data/log.json
	mv ./front/chart/data/orders* ./front/chart/data/orders.json
	mv ./front/chart/data/price_history* ./front/chart/data/price_history.json

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

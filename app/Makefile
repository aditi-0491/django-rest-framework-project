REPO_DIR= $(shell cd ../ && pwd)

.PHONY: build
build: ## Build the Docker images to prepare for runtime.
	@printf '\033[33m';
	@echo ------------------------------------
	@echo - Building the FoodLog Docker Image -
	@echo ------------------------------------
	@printf '\033[0m';
	docker-compose build --no-cache && docker image prune -f

.PHONY: up
up: ## Start all containers in foreground.
	@printf '\033[33m';
	@echo --------------------------------------
	@echo - Starting the FoodLog containers -
	@echo --------------------------------------
	@printf '\033[0m';
ifeq ($(shell docker network ls | grep food > /dev/null && echo yes), yes)
	@echo Network food exists, proceed with docker-compose  up
else
	make network
endif
	docker-compose up
	make down
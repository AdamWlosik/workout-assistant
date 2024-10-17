.DEFAULT_GOAL := help
.PHONY: help
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: shell
shell:  ## Uruchom shell poetry
	poetry shell

#.PHONY: migrations
#migrations: ## Utwórz migracie
#	@ (cd src && python manage.py makemigrations)
#
#.PHONY: migrate
#migrate: ## Zmigruj baze
#	cd src && python manage.py migrate
#
#.PHONY: migall
#migall: migrations migrate ## Utwórz migracie i zmigruj baze

.PHONY: test
test: ## Uruchom test
	cd src && python manage.py test

#.PHONY: run
#run: ## Uruchom aplikacje
#	cd src && python manage.py runserver

#.PHONY: createapp
#createapp: ## Utwórz nowa aplikacje w projekcie
#	cd src && #TODO

.PHONY: format
format: ## Ruff formatowanie i sprawdzanie
	ruff format && ruff check --fix

.PHONY: createapp
createapp: ## Utwórz nowa aplikacje w projekcie
	@read -p "Filename: " APP_NAME \
	&& cd src && python manage.py startapp $${APP_NAME} \
	&& echo "createdapp: $${APP_NAME}"

#.PHONY: logs
#logs: ## Idź za logami dockera
#	docker compose logs -f

.PHONY: shell-web
shell-web: ## Idź do shella serwisu web
	docker compose exec web /bin/sh

.PHONY: migrations
migrations: ## Utwórz migracie
	@ (cd src && docker compose exec web python manage.py makemigrations)

.PHONY: migrate
migrate: ## Zmigruj baze
	cd src && docker compose exec web python manage.py migrate

.PHONY: migall
migall: migrations migrate ## Utwórz migracie i zmigruj baze

.PHONY: run
run: ## Uruchom aplikacje
	cd src && docker compose up

.PHONY: build_image
build_image: ## Zbuduj image
	cd src && docker compose build

.PHONY: logs
logs: ## Wyswietl logi
	cd src && docker compose logs -f

.PHONY: ps
ps: ##
	cd src && docker compose ps

.PHONY: restart
restart: ## Zrestartuj applikacje
	cd src && docker compose down && docker compose up -d

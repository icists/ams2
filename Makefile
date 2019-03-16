SHELL := /bin/bash -e

.DEFAULT_GOAL := help

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[0-9a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

migrate: ## Build the schema/tables in dynamo
	go run ./cmd/db/migrate/migrate.go


CONTAINERS = django web mysql

# $(CONTAINERS): ## docker-compose를 통해 $@
#	@echo ssh-into $@...
#	docker exec -i -t $@ /bin/sh


ssh-into-django: ## docker-compose를 통해 실행 중일 때 shell로 django 컨테이너에 접근합니다.
	docker exec -i -t django /bin/ash

ssh-into-web: ## docker-compose를 통해 실행 중일 때 shell로 web 컨테이너에 접근합니다.
	docker exec -i -t web /bin/bash

ssh-into-mysql: ## docker-compose를 통해 실행 중일 때 shell로 mysql 컨테이너에 접근합니다.
	docker exec -i -t mysql /bin/bash

deploy-local: ## Local에서 실행
	docker-compose up -d --force-recreate


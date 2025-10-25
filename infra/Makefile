.PHONY: up down logs shell

up:
	docker-compose -f infra/docker-compose.yml up --build

down:
	docker-compose -f infra/docker-compose.yml down

logs:
	docker-compose -f infra/docker-compose.yml logs -f

shell-backend:
	docker exec -it aeza-backend /bin/bash

shell-agent:
	docker exec -it aeza-agent /bin/bash

shell-frontend:
	docker exec -it aeza-frontend /bin/bash


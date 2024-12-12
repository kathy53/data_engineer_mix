bash:
	docker run --rm -it -v $(shell pwd):/usr/src/app --env-file ./.env -p 8000:8000 api_books /bin/bash

build:
	docker build -t api_books .
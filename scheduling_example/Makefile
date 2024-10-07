jupyter:
	docker run --rm -it -p 8888:8888 -v $(shell pwd):/usr/src/app ndcompanies_crawler_playwright 

bash:
	docker run --rm -it -v $(shell pwd):/usr/src/app --env-file ./.env ndcompanies_crawler_playwright /bin/bash

build:
	docker build -t ndcompanies_crawler_playwright .
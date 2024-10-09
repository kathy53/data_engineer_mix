jupyter:
	docker run --rm -it -p 8888:8888 -v $(shell pwd):/usr/src/app gspread_up 

bash:
	docker run --rm -it -v $(shell pwd):/usr/src/app --env-file ./.env gspread_up /bin/bash

build:
	docker build -t gspread_up .
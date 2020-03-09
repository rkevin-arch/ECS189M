all: build
build:
	docker build -t finalwebapp . && docker run -it --rm -v `pwd`/templates:/home/web/templates -v `pwd`/app.py:/home/web/app.py -p 8080:8080 finalwebapp

run:
	docker run -it --rm -v `pwd`/templates:/home/web/templates -v `pwd`/app.py:/home/web/app.py -v `pwd`/static:/home/web/static -p 8080:8080 finalwebapp


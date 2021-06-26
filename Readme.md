FLASK Image  Demo
================================

build:

    docker build -t myflask .

run:

    docker run -ti -p 8080:8080 -e PORT=8080 myflask

FLASK Image  Demo
================================

build:

    docker build -t myflask .

run:

    docker run -ti -p 8080:8080 -e PORT=8080 myflask


API
===

curl -X GET http://localhost/blog/blog_title -  Show post

curl -X DELETE http://localhost/blog/blog_title - Delete Post

curl -X POST http://localhost/ -d {"title":"post_title", "description": "post_description", "create":"2021-06-27 13:35", "author":"author_name"}  - Add Post

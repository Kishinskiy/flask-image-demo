from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
api = Api(app)

DB_URL = os.getenv('DB')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)


class Blogs(db.Model):
    title = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime)
    author = db.Column(db.String(50))

    def __repr__(self):
        return '<Blogs %r>' % self.title


db.create_all()


class SaveBlog(Resource):

    def post(self):
        blog_title = request.form['title']
        blog_description = request.form['description']
        blog_created = request.form['created']
        blog_author = request.form['author']

        db_data = Blogs(title=blog_title,
                        description=blog_description,
                        created=blog_created,
                        author=blog_author)
        db.session.add(db_data)
        db.session.commit()

        return {'status': 201}


class ShowBlog(Resource):
    def get(self, blog_id):
        blog = Blogs.query.filter_by(title=blog_id).first_or_404(
            description='The Blog with title {} not found'.format(blog_id))

        return {
            'title': blog.title,
            'description': blog.description,
            'created': str(blog.created),
            'author': blog.author
        }, {'status': 201}

    def delete(self, blog_id):
        blog = Blogs.query.filter_by(title=blog_id).first_or_404(
            description='The Blog with title {} not found'.format(blog_id))
        db.session.delete(blog)
        db.session.commit()
        return {'status': 204}

api.add_resource(SaveBlog, '/')
api.add_resource(ShowBlog, '/blog/<blog_id>')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

import os
from datetime import datetime

from flask import Flask, render_template
from flask_pydantic import validate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel

app = Flask(__name__)
api = Api(app)

PORT = os.getenv('PORT')
DEBUG = os.getenv('DEBUG')
DB_URL = os.getenv('DB')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)


class BodyModel(BaseModel):
    title: str
    description: str
    created: datetime
    author: str


class Blogs(db.Model):
    title = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    author = db.Column(db.String(50))

    def __repr__(self):
        return '<Blogs %r>' % self.title


db.create_all()

@app.route('/')
def home():
   return render_template('base.html')

@app.route('/blog', methods=['POST'])
@validate()
def push_post(body: BodyModel):
    blog_title = body.title
    blog_description = body.description
    blog_created = body.created
    blog_author = body.author

    db_data = Blogs(title=blog_title,
                    description=blog_description,
                    created=blog_created,
                    author=blog_author)
    db.session.add(db_data)
    db.session.commit()

    return {'status': 201}


@app.route('/blog/<string:post_title>', methods=['GET'])
def get_posts(post_title):
    blog = Blogs.query.filter_by(title=post_title).first_or_404(
        description='The Blog with title {} not found'.format(post_title))

    return {
               'title': blog.title,
               'description': blog.description,
               'created': str(blog.created),
               'author': blog.author
           }, {'status': 201}


@app.route('/blog/<post_title>', methods=['DELETE'])
def delete(post_title):
    blog = Blogs.query.filter_by(title=post_title).first_or_404(
        description='The Blog with title {} not found'.format(post_title))
    db.session.delete(blog)
    db.session.commit()
    return {'status': 204}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)

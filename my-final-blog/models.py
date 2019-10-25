from  exist import db
from datetime import datetime
class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(10),nullable=False)
    password = db.Column(db.String(100),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref=db.backref('articles'))

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    review_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    reviewer_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    article = db.relationship('Article',backref=db.backref('reviews'))
    author = db.relationship('User',backref=db.backref('reviews'))
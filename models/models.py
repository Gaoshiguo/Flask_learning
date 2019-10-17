from exist import db

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(20),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref = db.backref('articles'))

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.Integer,nullable=False)
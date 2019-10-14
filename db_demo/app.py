from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
#在MySQL中如何创建一张表
# create table articles{
#     id :  int, primarykey,autoincrement;      #id是一个Int类型，主键，递增
#     title:varchar,not null;           #title是一个可变字符串类型，非空
#     content:text,not null         #content是一个text类型，非空
# }
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

db.create_all()

@app.route('/')
def hello_world():
    #数据库的增删改查
    ##增加数据
    # article1 = Article(title='four',content='this is four')
    # db.session.add(article1)
    #提交事务
    # db.session.commit()

    #查找数据
    #query查找的结果是以数组的方式存储的
    # result = Article.query.filter(Article.id == '2').all()
    # article=result[0]
    # print("id为%d的数据标题为:%s"%(article.id,article.title))
    # print("id为%d的数据的内容为:%s"%(article.id,article.content))
    #更改数据
    #1.先查找出需要更改的数据
    #2.更改数据
    #3.提交数据
    # result = Article.query.filter(Article.id == '2').all()
    # result[0].title = 'update'
    # db.session.commit()

    #删除数据
    #1.先查找出需要删除的数据
    #2.删除数据
    #3.提交事务
    result = Article.query.filter(Article.id == '1').first()
    db.session.delete(result)
    db.session.commit()



    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)

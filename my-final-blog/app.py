from flask import Flask,render_template,request,session,redirect,url_for
import config
from models import User,Article,Review
from exist import db
from functools import wraps
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

def login_restrict(fun):
    @wraps(fun)
    def restrict(*args,**kwargs):
        if session.get('user_id'):
            return fun(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return restrict




@app.route('/')
def index():
    content = {
        'articles':Article.query.all()
    }

    return render_template('index.html',**content)

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username,User.password==password).first()
        if user:
            session['user_id']=user.id
            session.permanent=True
            return redirect(url_for('index'))
        else:
            return "用户名或密码错误！"


@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter(User.username==username).first()
        #判断注册的用户名是否重复
        if user:
            return "该用户名已被使用，请重新注册！"
        #判断两次输入的密码是否一样
        else:
            if password1 != password2:
                return "两次输入的密码不一致！"
            else:
                user = User(username=username,password = password1)
                db.session.add(user)
                db.session.commit()
                #注册成功后，自动跳转到登陆页面（重定向）
                return  redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))



@app.context_processor
def context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id==user_id).first()
        if user:
            return {'user':user}
    return {}

@app.route('/article/',methods=['GET','POST'])
@login_restrict
def article():
    if request.method=='GET':
        return render_template('article.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        article = Article(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        article.author = user
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/detail/<article_id>/')
def detail(article_id):
    article1=Article.query.filter(Article.id==article_id).first()
    return render_template('detail.html',article=article1)

@app.route('/review/',methods=['POST'])
@login_restrict
def review():
    content = request.form.get('review-content')
    article_id = request.form.get('article_id')
    review = Review(content=content)
    user = session.get('user_id')
    author = User.query.filter(User.id==user).first()
    article = Article.query.filter(Article.id==article_id).first()
    review.article=article
    review.author=author
    db.session.add(review)
    db.session.commit()
    return redirect(url_for('detail',article_id=article_id))



if __name__ == '__main__':
    app.run(debug=True)

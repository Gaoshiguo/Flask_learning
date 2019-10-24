from flask import Flask,render_template,request,session,redirect,url_for
import config
from models import User
from exist import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username,User.password==password).first()
        if user:
            session['userid']=user.id
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
if __name__ == '__main__':
    app.run(debug=True)

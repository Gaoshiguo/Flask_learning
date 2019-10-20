from flask import Flask,session,render_template,request
import os
from datetime import timedelta
app = Flask(__name__)
app.config['SECRET_KEY']= os.urandom(24)
app.config['PERNAMENT_SESSION_LIFETIEM']=timedelta(days=7)
# @app.route('/')
# def hello_world():
#     session['username']='gao'
#     #如果没有设置过期时间，系统默认为关闭浏览器即过期
#     #设置过期时间,系统默认当session.permanent = True时是31天，如果想要更改为自己想要的时间需要加入app.config['PERNAMENT_SESSION_LIFETIEM']=timedelta(days=7)
#     session.permanent = True
#     return 'Hello World!'
# @app.route('/get/')
# def get():
#     return '当前的cookie值为username:'+session.get('username')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/')
def search():
    s=request.args.get("q")
    print("get请求得参数是",s)
    return render_template('search.html')


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        return "用户名是：%s密码是：%s"%(username,password)

if __name__ == '__main__':
    app.run(debug=True)

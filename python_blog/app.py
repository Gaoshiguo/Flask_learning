from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '这是首页!'

@app.route('/articles/<id>')
def show_articles(id):
	return '您请求的文章id是%s'%id
@app.route('/blog/')
def blog():
	return '这是发布文章页面!!!'
@app.route('/login/')
def login():
	return '这是登录页面,请登录!!!'

@app.route('/blog/<id>')
def redi_ct(id):
	if id=='1':
		return '这是发布文章页面!'
	else:
		return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

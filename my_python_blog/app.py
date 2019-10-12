from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)


@app.route('/')
def index():
	class person(object):
		name='gao'
		age='18'

	p = person()
	parameter ={
	'username':'高手',
	'age':'18',
	'gender':'男',
	'height':'180cm',
	'person':p,
	'website':{
	'简书':'www.jianshu.com',
	'CSDN':'www.csdn.com',
	}
	}
	return render_template('index.html',**parameter)

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

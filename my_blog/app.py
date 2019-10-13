from flask import Flask,render_template

app = Flask(__name__)


@app.route('/<is_login>/')
def index(is_login):
	if is_login=='1':
		users = [
		{
		'username':'高小帅',
		'age':18,
		'gender':'male',
		},
		{
		'username':'高美丽',
		'age':19,
		'gender':'female',
		},
		{
		'username':'赵日天',
		'age':25,
		'gender':'male',
		},
		]
		return render_template('index.html',user=users)
	else:
		return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

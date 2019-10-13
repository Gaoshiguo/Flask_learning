from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
	comment=[
	{
	'username':'吴彦祖',
	'content':'哎哟不错哦!'
	},
	{
	'username':'刘德华',
	'content':'给我一杯忘情水!'
	},
	{
	'username':'李宇春',
	'content':'信春哥得永生!'
	},

	]
	return render_template('new_index.html',comment=comment)
	

if __name__ == '__main__':
    app.run(debug=True)

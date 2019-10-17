from flask import Flask,render_template
import config
from exist import db
from models import Article


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

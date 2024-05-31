from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
admin = Admin()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)

admin.add_view(ModelView(User, db.session))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbw.sqlite3'
    app.config['SECRET_KEY'] = '77fbfbeb-2ab4-4cc7-af84-ac3d84dd9035'

    db.init_app(app)
    admin.init_app(app)

    return app

app = create_app()

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

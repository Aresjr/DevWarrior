import os

from flask import Flask
from extensions import db, admin
from routes import main


def create_app():
    app = Flask(__name__)
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbw.sqlite3'
    app.config['SECRET_KEY'] = os.environ.get('DBW_KEY')

    app.register_blueprint(main)

    db.init_app(app)
    admin.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

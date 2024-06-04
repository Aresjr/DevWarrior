from flask import Blueprint, render_template
from models import User, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/@<username>')
def hello(username):
    user = db.session.query(User).filter_by(username=username).first()
    return user.name

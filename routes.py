from flask import Blueprint
from models import User, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'Index Page'

@main.route('/user/<username>')
def hello(username):
    user = db.session.query(User).filter_by(username=username).first()
    return user.name

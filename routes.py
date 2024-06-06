from flask import Blueprint, render_template
from initializr import initialize
from models import User, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/@<username>')
def hello(username):
    user = db.session.query(User).filter_by(username=username).first()
    return user.name

@main.route('/create_db')
def create_db():
    db.create_all()
    return 'Database created'

@main.route('/drop_db')
def drop_db():
    db.drop_all()
    return 'Database dropped'

@main.route('/initialize')
def initialize_db():
    initialize()
    return 'Database initialized'

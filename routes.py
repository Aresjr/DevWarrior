from flask import Blueprint, render_template
from database import db
from models.user import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/@<username>')
def hello(username):
    user = db.session.query(User).filter_by(username=username).first()
    if not user:
        return 'User not found'
    return user.full_title()

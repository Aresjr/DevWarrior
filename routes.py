from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'Index Page'

@main.route('/hello')
def hello():
    return 'Hello, World'

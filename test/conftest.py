import pytest
from app import create_app
from database import db
from initializr import initialize
from models.skills import Skill, SkillCategory
from models.user import Class, Title


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

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

def test_initialize(app):
    with app.app_context():
        db.create_all()
        if db.session.query(SkillCategory).count() == 0:
            initialize()

        assert db.session.query(Skill).count() > 0
        assert db.session.query(SkillCategory).count() > 0
        assert db.session.query(Class).count() > 0
        assert db.session.query(Title).count() > 0

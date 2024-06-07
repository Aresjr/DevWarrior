from database import db
from initializr import initialize
from models.skills import SkillCategory, Skill
from models.user import Class, Title


def test_initialize_skill_category(app):
    with app.app_context():
        db.create_all()
        if db.session.query(SkillCategory).count() == 0:
            initialize()

        assert db.session.query(SkillCategory).count() > 0

def test_initialize_skill(app):
    with app.app_context():
        db.create_all()
        if db.session.query(Skill).count() == 0:
            initialize()

        assert db.session.query(Skill).count() > 0

def test_initialize_class(app):
    with app.app_context():
        db.create_all()
        if db.session.query(Class).count() == 0:
            initialize()

        assert db.session.query(Class).count() > 0

def test_initialize_title(app):
    with app.app_context():
        db.create_all()
        if db.session.query(Title).count() == 0:
            initialize()

        assert db.session.query(Title).count() > 0

from database import db
from initializr import initialize
from models.skills import SkillCategory, Skill
from models.user import Class, Title


def test_initialize():
    db.create_all()
    initialize()
    assert db.session.query(Skill).count() > 0
    assert db.session.query(SkillCategory).count() > 0
    assert db.session.query(Class).count() > 0
    assert db.session.query(Title).count() > 0

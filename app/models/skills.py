from app.database import db

class SkillCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    skills = db.relationship('Skill', back_populates='category', lazy=True)

    def __str__(self):
        return self.name

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('skill_category.id'), nullable=True)
    category = db.relationship('SkillCategory', back_populates='skills', lazy=True)
    users = db.relationship('UserSkill', back_populates='skill', lazy=True)

    def __str__(self):
        return self.name

class UserSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    user = db.relationship('User', back_populates='skills', lazy=True)
    skill = db.relationship('Skill', back_populates='users', lazy=True)

    def __str__(self):
        return self.skill.name

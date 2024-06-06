from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=True)
    class_ = db.relationship('Class', back_populates='users', lazy=True)
    skills = db.relationship('UserSkill', back_populates='user', lazy=True)

    def __str__(self):
        return self.username

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    users = db.relationship('User', back_populates='class_', lazy=True)

    def __str__(self):
        return self.name

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

class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    initial_date = db.Column(db.Date, nullable=False)
    final_date = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return self.description

class SideQuest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    initial_date = db.Column(db.Date, nullable=False)
    final_date = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return self.description

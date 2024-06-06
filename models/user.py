from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'), nullable=True)
    level = db.Column(db.Integer, nullable=True, default=1)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'), nullable=True)
    class_ = db.relationship('Class', back_populates='users', lazy=True)
    skills = db.relationship('UserSkill', back_populates='user', lazy=True)
    title = db.relationship('Title', back_populates='users', lazy=True)

    def full_title(self):
        return "Level " + str(self.level) + " " + self.title.name + " " + self.class_.name

    def __str__(self):
        return self.username

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    users = db.relationship('User', back_populates='class_', lazy=True)

    def __str__(self):
        return self.name

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    users = db.relationship('User', back_populates='title', lazy=True)

    def __str__(self):
        return self.name

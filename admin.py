from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Skill, SkillCategory, UserSkill, Class

admin = Admin()

class UserView(ModelView):
    can_delete = False
    form_columns = ['name', 'username', 'password', 'email', 'class_',  'skills']
    column_list = ['name', 'username', 'email', 'class_', 'skills']

class ClassView(ModelView):
    can_delete = True
    form_columns = ['name']
    column_list = ['name', 'users']

class UserSkillView(ModelView):
    form_columns = ['user', 'skill', 'level']
    column_list = ['user', 'skill', 'level']

class SkillView(ModelView):
    can_delete = True
    form_columns = ['name', 'category']
    column_list = ['name', 'category']

class SkillCategoryView(ModelView):
    can_delete = True
    form_columns = ['name']
    column_list = ['name', 'skills']

admin.add_view(UserView(User, db.session))
admin.add_view(ClassView(Class, db.session))
admin.add_view(UserSkillView(UserSkill, db.session))
admin.add_view(SkillView(Skill, db.session))
admin.add_view(SkillCategoryView(SkillCategory, db.session))


from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User, Skill, SkillCategory

admin = Admin()

class UserView(ModelView):
    can_delete = False

class SkillView(ModelView):
    can_delete = True
    form_columns = ['name', 'category']
    column_list = ['name', 'category']

class SkillCategoryView(ModelView):
    can_delete = True
    form_columns = ['name']
    column_list = ['name', 'skills']

admin.add_view(UserView(User, db.session))
admin.add_view(SkillView(Skill, db.session))
admin.add_view(SkillCategoryView(SkillCategory, db.session))

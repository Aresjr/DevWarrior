from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models.skills import UserSkill, Skill, SkillCategory
from .models.user import User, Class, Title
from .database import db

admin = Admin()

class UserView(ModelView):
    can_delete = False
    form_columns = ['name', 'username', 'password', 'email', 'class_',  'skills', 'title']
    column_list = ['name', 'username', 'email', 'class_', 'skills', 'title', 'level']

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

class TitleView(ModelView):
    can_delete = True
    form_columns = ['name']
    column_list = ['name', 'users']

admin.add_views(UserView(User, db.session), ClassView(Class, db.session), UserSkillView(UserSkill, db.session),
                SkillView(Skill, db.session), SkillCategoryView(SkillCategory, db.session),
                TitleView(Title, db.session))

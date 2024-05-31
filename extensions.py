from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User

admin = Admin()

class ModelViewW(ModelView):
    can_delete = False

admin.add_view(ModelViewW(User, db.session))

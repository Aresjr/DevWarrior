from models import db
from sqlalchemy import event


# @event.listens_for(QuestType.__table__, 'after_create')
# def create_departments(*args, **kwargs):
#     db.session.add(QuestType(name='Quests (Experiences)'))
#     db.session.add(QuestType(name='Side Quests (Freelances)'))
#     db.session.commit()

from . import *
from models.lesson import Lesson

class Company(db.Document):
# class Company(db.Model, ModelMixin):
    # __tablename__ = 'companies'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String())
    # logo_path = db.Column(db.String())
    # lessons = db.relationship('Lesson', backref='company')

    name = db.StringField()
    logo_path = db.StringField()
    lessons = db.ListField(ReferenceField(Lesson))

    # def __init__(self, form):
    #     name = form.get('name', '')
    #     logo_path = form.get('logo_path', '')
    #     self = Company(name=name, logo_path=logo_path)
    #     self.save()

    def insert_lesson(self, lesson):
        self.update(add_to_set__lessons=[lesson])
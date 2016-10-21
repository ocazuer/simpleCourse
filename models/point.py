from . import ModelMixin
from . import db
from . import timestamp

class Point(db.Model, ModelMixin):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    target = db.Column(db.String())
    content = db.Column(db.String())
    created_time = db.Column(db.Integer)
    updated_time = db.Column(db.Integer)

    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))

    def __init__(self, form):
        self.created_time = timestamp()
        self.updated_time = timestamp()
        self.name = form.get('name', '')
        self.target = form.get('target', '')
        self.content = form.get('content', '')
        self.lesson_id = form.get('lesson_id', '')
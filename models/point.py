from . import ModelMixin
from . import db
from . import timestamp

class Point(db.Model, ModelMixin):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    target = db.Column(db.String())
    content = db.Column(db.String())

    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))

    def __init__(self, form):
        self.username = form.get('username', '')
        self.target = form.get('target', '')
        self.content = form.get('content', '')

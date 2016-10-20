from . import ModelMixin
from . import db
from . import timestamp

def Point(db.Model, ModelMixin):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Interger)
    target = db.Column(db.Interger)
    content = db.Column(db.Interger)

    lesson_id = db.Column(db.Interger, db.ForeignKey='lesson.id')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.target = form.get('target', '')
        self.content = form.get('content', '')

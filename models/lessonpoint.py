from . import ModelMixin
from . import db
from . import timestamp

def lesson(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Interger)
    target = db.Column(db.Interger)
    content = db.Column(db.Interger)

    def __init__(self, form):
        self.username = form.get('username', '')
        self.target = form.get('target', '')
        self.content = form.get('content', '')

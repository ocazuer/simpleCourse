from . import ModelMixin
from . import db
from . import timestamp

def User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Interger)

    def __init__(self, form):
        self.username = form.get('username', '')

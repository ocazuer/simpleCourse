from . import ModelMixin
from . import db
from . import timestamp

def Company(db.Model, ModelMixin):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Interger)
    logo_path = db.Column(db.Interger)

    def __init__(self, form):
        self.name = form.get('name', '')
        self.logo_path = form.get('logo_path', '')
from . import ModelMixin
from . import db
from . import timestamp
from models.company import Company

class Lesson(db.Model, ModelMixin):
    __tablename__ = 'lessons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    points = db.relationship('Point', backref='lesson')

    def __init__(self, form):
        self.name = form.get('name', '')
        self.company_id = form.get('company_id', '')
        
from . import ModelMixin
from . import db
from . import timestamp

class Lesson(db.Model, ModelMixin):
    __tablename__ = 'lessons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    points = db.relationship('Point', backref='lesson')

    def __init__(self, form):
        self.username = form.get('username', '')
        self.target = form.get('target', '')
        self.content = form.get('content', '')

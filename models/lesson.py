from . import ModelMixin
from . import db
from . import timestamp
from models.company import Company
# from functools import cmp_to_key
from operator import itemgetter, attrgetter

class Lesson(db.Model, ModelMixin):
    __tablename__ = 'lessons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    points = db.relationship('Point', backref='lesson')

    def __init__(self, form):
        self.name = form.get('name', '')
        self.company_id = form.get('company_id', '')

    def get_points_by_updated_time(self):
        points = self.points
        # points.sorted(lambda p1, p2:cmp(p1.updated_time, p2.updated_time))
        sorted(points, key=attrgetter('created_time', 'id'))
        return points or []
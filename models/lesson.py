from . import *
from models.point import Point
from operator import itemgetter, attrgetter

class Lesson(db.Document):
    # __tablename__ = 'lessons'
    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String())
    # company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    # points = db.relationship('Point', backref='lesson')

    name = db.StringField()
    points = db.ListField(ReferenceField(Point))

    # def __init__(self, form):
    #     self.name = form.get('name', '')
    #     self.save()

    def insert_point(self, point):
        self.save()
        self.update(add_to_set__points=[point])
        self.save()

    def get_points_by_updated_time(self):
        points = self.points
        # points.sorted(lambda p1, p2:cmp(p1.updated_time, p2.updated_time))
        sorted(points, key=attrgetter('created_time', 'id'))
        return points or []
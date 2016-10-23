from flask_sqlalchemy import SQLAlchemy
import time
from flask_mongoengine import MongoEngine
from mongoengine import ReferenceField
from flask_mongoengine.wtf import model_form

# db = SQLAlchemy()
db = MongoEngine()


def timestamp():
    return int(time.time())


class ModelMixin(object):
    def save(self):
        self.save()

    # def delete(self):
    #     self.remove()

    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
    #     return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
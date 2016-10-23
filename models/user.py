from . import *
from models.lesson import Lesson

import hashlib

def hash_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(db.Document):
    # __tablename__ = 'users'
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(), unique=True)
    # # md5 密文储存密码
    # password = db.Column(db.String())

    username = db.StringField()
    password = db.StringField()

    # def __init__(self, form):
    #     self.username = form.get('username', '')
    #     self.password = hash_md5(form.get('password', ''))
    #     self.save()

    def validate_register(self):
        c1 = len(self.username) >= 2
        c2 = len(self.username) <= 20
        return c1 and c2

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password
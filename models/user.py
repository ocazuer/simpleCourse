from . import ModelMixin
from . import db
from . import timestamp

import hashlib

def hash_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    # md5 密文储存密码
    password = db.Column(db.String())

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = hash_md5(form.get('password', ''))

    def validate_register(self):
        c1 = len(self.username) >= 2
        c2 = len(self.username) <= 20
        # c3 = User.query.filter_by(username=self.username).first() is None
        # return c1 and c2 and c3
        return c1 and c2

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password
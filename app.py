import sys

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# from flask.ext.mongoalchemy import MongoAlchemy
from flask_mongoengine import MongoEngine

from models import db
from models.company import Company
from models.lesson import Lesson
from models.point import Point
from models.user import User

from routes.index import main as route_index
from routes.user import main as route_user
from routes.lesson import main as route_lesson
from routes.company import main as route_company

app = Flask(__name__)
# db_path = 'simplecourse.sqlite'
manager = Manager(app)


def register_routes(app):
    app.register_blueprint(route_index, url_prefix='/')
    app.register_blueprint(route_user, url_prefix='/user')
    app.register_blueprint(route_lesson, url_prefix='/lesson')
    app.register_blueprint(route_company, url_prefix='/company')


def configure_app():
    app.config['SECRET_KEY'] = 'flask+mongoengine=<3'
    # db = MongoAlchemy(app)
    register_routes(app)
    db = MongoEngine(app)

def configured_app():
    configure_app()
    return app


# 自定义的命令行命令用来运行服务器
@manager.command
def server():
    print('server run')
    if sys.platform == 'linux':
        port = 80
    else:
        port = 2000
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=port,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
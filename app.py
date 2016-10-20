import sys

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db
from models.company import Company
from models.lessonpoint import Lessonpoint
from models.user import User

app = Flask(__name__)
db_path = 'simplecourse.sqlite'
manager = Manager(app)


def register_routes(app):
    app.register_blueprint('')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    db.init_app(app)
    register_routes(app)


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
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app

from app.api import blueprint
from app.repository.database import db
from app.models.todo import Todo

app = create_app('dev')
db.init_app(app)
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'])

@manager.command
def test():
    import pytest
    return pytest.main(['-vx', 'app/tests'])

if __name__ == '__main__':
    manager.run()